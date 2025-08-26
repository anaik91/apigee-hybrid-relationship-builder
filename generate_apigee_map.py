import sys
import argparse
from collections import deque
from kubernetes import client, config

# --- Configuration ---
HELM_ANNOTATION_RELEASE_NAME = "meta.helm.sh/release-name"
HELM_ANNOTATION_RELEASE_NAMESPACE = "meta.helm.sh/release-namespace"


RESOURCE_METADATA = {
    # Namespaced resources
    "Pod": {"scope": "namespaced", "fetcher": lambda api, n: api["v1"].list_namespaced_pod(n).items},
    "Deployment": {"scope": "namespaced", "fetcher": lambda api, n: api["apps_v1"].list_namespaced_deployment(n).items},
    "HorizontalPodAutoscaler": {"scope": "namespaced", "fetcher": lambda api, n: api["hpa"].list_namespaced_horizontal_pod_autoscaler(n).items},
    "ReplicaSet": {"scope": "namespaced", "fetcher": lambda api, n: api["apps_v1"].list_namespaced_replica_set(n).items},
    "StatefulSet": {"scope": "namespaced", "fetcher": lambda api, n: api["apps_v1"].list_namespaced_stateful_set(n).items},
    "DaemonSet": {"scope": "namespaced", "fetcher": lambda api, n: api["apps_v1"].list_namespaced_daemon_set(n).items},
    "Service": {"scope": "namespaced", "fetcher": lambda api, n: api["v1"].list_namespaced_service(n).items},
    "ConfigMap": {"scope": "namespaced", "fetcher": lambda api, n: api["v1"].list_namespaced_config_map(n).items},
    "Secret": {"scope": "namespaced", "fetcher": lambda api, n: api["v1"].list_namespaced_secret(n).items},
    "ServiceAccount": {"scope": "namespaced", "fetcher": lambda api, n: api["v1"].list_namespaced_service_account(n).items},
    "Role": {"scope": "namespaced", "fetcher": lambda api, n: api["rbac_v1"].list_namespaced_role(n).items},
    "RoleBinding": {"scope": "namespaced", "fetcher": lambda api, n: api["rbac_v1"].list_namespaced_role_binding(n).items},
    "Certificate": {"scope": "namespaced", "fetcher": lambda api, n: api["custom"].list_namespaced_custom_object("cert-manager.io", "v1", n, "certificates").get("items", [])},
    # Apigee CRDs
    "ApigeeOrganization": {"scope": "namespaced", "fetcher": lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha2", n, "apigeeorganizations").get("items", [])},
    "ApigeeEnvironment": {"scope": "namespaced", "fetcher": lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha2", n, "apigeeenvironments").get("items", [])},
    "ApigeeDeployment": {"scope": "namespaced", "fetcher": lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha3", n, "apigeedeployments").get("items", [])},
    "ApigeeRedis": {"scope": "namespaced", "fetcher": lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha1", n, "apigeeredis").get("items", [])},
    "ApigeeDatastore": {"scope": "namespaced", "fetcher": lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha1", n, "apigeedatastores").get("items", [])},
    "ApigeeIssue": {"scope": "namespaced", "fetcher": lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha1", n, "apigeeissues").get("items", [])},
    "ApigeeRouteConfig": {"scope": "namespaced", "fetcher": lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha1", n, "apigeerouteconfigs").get("items", [])},
    "ApigeeRoute": {"scope": "namespaced", "fetcher": lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha2", n, "apigeeroutes").get("items", [])},
    "ApigeeTelemetry": {"scope": "namespaced", "fetcher": lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha2", n, "apigeetelemetries").get("items", [])},
    "CassandraDatareplication": {"scope": "namespaced", "fetcher": lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha1", n, "cassandradatareplications").get("items", [])},
    "SecretRotation": {"scope": "namespaced", "fetcher": lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha1", n, "secretrotations").get("items", [])},
    # Cluster-scoped resources
    "MutatingWebhookConfiguration": {"scope": "cluster", "fetcher": lambda api: api["wh_v1"].list_mutating_webhook_configuration().items},
    "ValidatingWebhookConfiguration": {"scope": "cluster", "fetcher": lambda api: api["wh_v1"].list_validating_webhook_configuration().items},
    "ClusterRole": {"scope": "cluster", "fetcher": lambda api: api["rbac_v1"].list_cluster_role().items},
    "ClusterRoleBinding": {"scope": "cluster", "fetcher": lambda api: api["rbac_v1"].list_cluster_role_binding().items},
    "ClusterIssuer": {"scope": "cluster", "fetcher": lambda api: api["custom"].list_cluster_custom_object("cert-manager.io", "v1", "clusterissuers").get("items", [])},
    "APIService": {"scope": "cluster", "fetcher": lambda api: api["apiregistration"].list_api_service().items}
}


KIND_TO_STYLE_GROUP = {
    "Deployment": "workload",
    "V2HorizontalPodAutoscaler": "workload",
    "StatefulSet": "workload",
    "DaemonSet": "workload",
    "ReplicaSet": "workload",
    "Pod": "workload",
    "Service": "network",
    "ConfigMap": "config",
    "Secret": "config",
    "ServiceAccount": "rbac",
    "Role": "rbac",
    "ClusterRole": "rbac",
    "RoleBinding": "rbac",
    "ClusterRoleBinding": "rbac",
    # Apigee CRDs
    "ApigeeOrganization": "apigee_crd",
    "ApigeeEnvironment": "apigee_crd",
    "ApigeeDeployment": "apigee_crd",
    "ApigeeRedis": "apigee_crd",
    "ApigeeDatastore": "apigee_crd",
    "ApigeeIssue": "apigee_crd",
    "ApigeeRouteConfig": "apigee_crd",
    "ApigeeRoute": "apigee_crd",
    "ApigeeTelemetry": "apigee_crd",
    "CassandraDatareplication": "apigee_crd",
    "SecretRotation": "apigee_crd",
    # Cert-Manager CRDs
    "Certificate": "cert_manager_crd",
    "ClusterIssuer": "cert_manager_crd",
    # Webhooks
    "MutatingWebhookConfiguration": "webhook",
    "ValidatingWebhookConfiguration": "webhook",
    "APIService": "webhook",
}

# Define the Mermaid styling for each group. You can change colors here.
STYLE_DEFINITIONS = {
    "helm": "classDef helm fill:#f9f,stroke:#333,stroke-width:2px,color:#000",
    "workload": "classDef workload fill:#cce5ff,stroke:#004085,stroke-width:1px,color:#000",
    "network": "classDef network fill:#d4edda,stroke:#155724,stroke-width:1px,color:#000",
    "config": "classDef config fill:#e2e3e5,stroke:#383d41,stroke-width:1px,color:#000",
    "rbac": "classDef rbac fill:#f8d7da,stroke:#721c24,stroke-width:1px,color:#000",
    "apigee_crd": "classDef apigee_crd fill:#fff3cd,stroke:#856404,stroke-width:2px,color:#000",
    "cert_manager_crd": "classDef cert_manager_crd fill:#d1ecf1,stroke:#0c5460,stroke-width:2px,color:#000",
    "webhook": "classDef webhook fill:#ddd,stroke:#333,stroke-width:2px,color:#000",
    "default": "classDef default fill:#fff,stroke:#333,stroke-width:1px,color:#000", # Fallback style
}


def get_possible_kinds():
    """Returns a sorted list of all resource Kinds the script knows about."""
    return sorted(list(RESOURCE_METADATA.keys()))

def _get_api_clients():
    """Helper to load kube config and initialize API clients."""
    try:
        config.load_kube_config()
        return {
            "v1": client.CoreV1Api(),
            "hpa" : client.AutoscalingV2Api(),
            "apps_v1": client.AppsV1Api(),
            "rbac_v1": client.RbacAuthorizationV1Api(),
            "custom": client.CustomObjectsApi(),
            "wh_v1" : client.AdmissionregistrationV1Api(),
            "apiregistration": client.ApiregistrationV1Api()
        }
    except Exception as e:
        print(f"Error: Could not configure Kubernetes client: {e}", file=sys.stderr)
        sys.exit(1)


def _fetch_all_potential_objects(api_clients, namespace):
    """Helper to fetch all defined resource types from the cluster."""
    all_potential_objects = []
    for kind, meta in RESOURCE_METADATA.items():
        try:
            if meta["scope"] == "namespaced":
                all_potential_objects.extend(meta["fetcher"](api_clients, namespace))
            else:
                all_potential_objects.extend(meta["fetcher"](api_clients))
        except client.ApiException as e:
            if e.status != 404:
                print(f"Warning: Could not fetch resource kind '{kind}': {e.reason}", file=sys.stderr)
    return all_potential_objects


def get_object_uid(k8s_object):
    if isinstance(k8s_object, dict):
        return k8s_object['metadata']['uid']
    else:
        return k8s_object.metadata.uid

def get_object_kind(k8s_object):
    if isinstance(k8s_object, dict):
        return k8s_object.get('kind', 'Unknown')
    else:
        kind = getattr(k8s_object, 'kind', None)
        if kind:
            return kind
        else:
            class_name = type(k8s_object).__name__
            return class_name.replace('V1', '').replace('V1beta1','')

def get_object_name(k8s_object):
    if isinstance(k8s_object, dict):
        return k8s_object['metadata']['name']
    else:
        return k8s_object.metadata.name

def get_object_spec(k8s_object):
    if isinstance(k8s_object, dict):
        return k8s_object.get('spec')
    else:
        return getattr(k8s_object, 'spec', None)


def discover_helm_managed_objects(api_clients, namespace, release_name):
    print("Fetching all potential resources for shallow discovery...")
    all_potential_objects = _fetch_all_potential_objects(api_clients, namespace)
    print(f"Identifying objects directly managed by release '{release_name}'...")
    seed_objects = []
    for obj in all_potential_objects:
        is_dict = isinstance(obj, dict)
        if is_dict:
            metadata = obj['metadata']
            annotations = metadata.get('annotations')
        else:
            metadata = obj.metadata
            annotations = metadata.annotations

        if annotations:
            is_release_match = annotations.get(HELM_ANNOTATION_RELEASE_NAME) == release_name
            is_namespace_match = annotations.get(HELM_ANNOTATION_RELEASE_NAMESPACE) == namespace
            if is_release_match and is_namespace_match:
                seed_objects.append(obj)
    return seed_objects


def discover_full_hierarchy(api_clients, namespace, release_name):
    print("Fetching all potential resources for deep discovery...")
    all_potential_objects = _fetch_all_potential_objects(api_clients, namespace)
    print(f"Identifying seed objects for release '{release_name}'...")
    seed_objects = []
    for obj in all_potential_objects:
        is_dict = isinstance(obj, dict)
        if is_dict:
            metadata = obj['metadata']
            annotations = metadata.get('annotations')
        else:
            metadata = obj.metadata
            annotations = metadata.annotations

        if annotations:
            is_release_match = annotations.get(HELM_ANNOTATION_RELEASE_NAME) == release_name
            is_namespace_match = annotations.get(HELM_ANNOTATION_RELEASE_NAMESPACE) == namespace
            if is_release_match and is_namespace_match:
                seed_objects.append(obj)

    if not seed_objects:
        return []

    print("Starting recursive discovery from seed objects...")
    final_objects = {}
    discovery_queue = deque(seed_objects)
    processed_uids = set()

    while discovery_queue:
        parent_obj = discovery_queue.popleft()
        parent_uid = get_object_uid(parent_obj)
        if parent_uid in processed_uids:
            continue
        processed_uids.add(parent_uid)
        final_objects[parent_uid] = parent_obj

        for child_obj in all_potential_objects:
            child_uid = get_object_uid(child_obj)
            if child_uid in processed_uids:
                continue

            is_dict = isinstance(child_obj, dict)
            if is_dict:
                metadata = child_obj['metadata']
                owner_refs = metadata.get('ownerReferences', [])
            else:
                metadata = child_obj.metadata
                if metadata.owner_references:
                    owner_refs = metadata.owner_references
                else:
                    owner_refs = []

            for owner in owner_refs:
                is_owner_dict = isinstance(owner, dict)
                if is_owner_dict:
                    owner_uid = owner.get('uid')
                else:
                    owner_uid = owner.uid

                if owner_uid == parent_uid:
                    discovery_queue.append(child_obj)
                    break
    return list(final_objects.values())


def build_relationship_map(all_objects, filtered_objects, release_name, namespace):
    print("Building relationship map...")
    relationships = []

    all_uids_to_objects = {}
    for obj in all_objects:
        all_uids_to_objects[get_object_uid(obj)] = obj

    filtered_uids = set()
    for obj in filtered_objects:
        filtered_uids.add(get_object_uid(obj))

    uid_to_node_id = {}
    for uid, obj in all_uids_to_objects.items():
        uid_to_node_id[uid] = f"{get_object_kind(obj)}/{get_object_name(obj)}"

    children_with_parents = set()

    def find_visible_parent_uid(child_obj):
        is_dict = isinstance(child_obj, dict)
        if is_dict:
            metadata = child_obj['metadata']
            owner_refs = metadata.get('ownerReferences')
        else:
            metadata = child_obj.metadata
            owner_refs = metadata.owner_references

        if not owner_refs:
            return None

        owner_ref = owner_refs[0]
        is_owner_ref_dict = isinstance(owner_ref, dict)
        if is_owner_ref_dict:
            current_owner_uid = owner_ref.get('uid')
        else:
            current_owner_uid = owner_ref.uid

        while current_owner_uid and current_owner_uid not in filtered_uids:
            parent_obj = all_uids_to_objects.get(current_owner_uid)
            if not parent_obj:
                current_owner_uid = None
                break

            is_parent_dict = isinstance(parent_obj, dict)
            if is_parent_dict:
                parent_metadata = parent_obj['metadata']
                parent_owner_refs = parent_metadata.get('ownerReferences')
            else:
                parent_metadata = parent_obj.metadata
                parent_owner_refs = parent_metadata.owner_references

            if parent_owner_refs:
                parent_owner_ref = parent_owner_refs[0]
                is_parent_owner_ref_dict = isinstance(parent_owner_ref, dict)
                if is_parent_owner_ref_dict:
                    current_owner_uid = parent_owner_ref.get('uid')
                else:
                    current_owner_uid = parent_owner_ref.uid
            else:
                current_owner_uid = None
        return current_owner_uid

    for obj in filtered_objects:
        child_id = uid_to_node_id.get(get_object_uid(obj))
        if not child_id:
            continue

        parent_id = None
        visible_parent_uid = find_visible_parent_uid(obj)
        if visible_parent_uid:
            parent_id = uid_to_node_id.get(visible_parent_uid)

        child_kind = get_object_kind(obj)
        if not parent_id and child_kind == 'ApigeeDeployment':
            spec = get_object_spec(obj)
            if spec and 'env' in spec:
                potential_parent_node_id = f"ApigeeEnvironment/{spec['env']}"
                parent_found = False
                for uid in filtered_uids:
                    if uid_to_node_id.get(uid) == potential_parent_node_id:
                        parent_found = True
                        break
                if parent_found:
                    parent_id = potential_parent_node_id

        if parent_id:
            relationships.append((parent_id, child_id))
            children_with_parents.add(child_id)

    for obj in filtered_objects:
        child_id = uid_to_node_id.get(get_object_uid(obj))
        if not child_id or child_id in children_with_parents:
            continue

        is_dict = isinstance(obj, dict)
        if is_dict:
            metadata = obj['metadata']
            annotations = metadata.get('annotations')
        else:
            metadata = obj.metadata
            annotations = metadata.annotations

        if annotations:
            is_release_match = annotations.get(HELM_ANNOTATION_RELEASE_NAME) == release_name
            is_namespace_match = annotations.get(HELM_ANNOTATION_RELEASE_NAMESPACE) == namespace
            if is_release_match and is_namespace_match:
                parent_id = f'Helm Release: {release_name}'
                relationships.append((parent_id, child_id))

    return relationships


def sanitize_node_id(node_id_str):
    sanitized = ""
    for char in node_id_str:
        if char.isalnum():
            sanitized += char
    return sanitized

def generate_mermaid_diagram(relationships, release_name):
    """
    Generates the Mermaid diagram with detailed, kind-based color coding.
    """
    print("Generating Mermaid diagram with color-coded kinds...")
    mermaid_lines = ["graph TD;"]

    for style_class in STYLE_DEFINITIONS.values():
        mermaid_lines.append(f'    {style_class}')
    mermaid_lines.append("")

    all_nodes = {}
    for owner_id, child_id in relationships:
        owner_node = sanitize_node_id(owner_id)
        child_node = sanitize_node_id(child_id)
        if owner_node not in all_nodes:
            all_nodes[owner_node] = owner_id
        if child_node not in all_nodes:
            all_nodes[child_node] = child_id
    
    for node_id, node_label in all_nodes.items():
         mermaid_lines.append(f'    {node_id}["{node_label}"]')
    mermaid_lines.append("")

    for node_id, node_label in all_nodes.items():
        style_group = "default"
        if node_label.startswith("Helm Release:"):
            style_group = "helm"
        else:
            kind = node_label.split('/')[0]
            if kind in KIND_TO_STYLE_GROUP:
                style_group = KIND_TO_STYLE_GROUP[kind]
        
        mermaid_lines.append(f'    class {node_id} {style_group};')
    mermaid_lines.append("")

    for owner_id, child_id in relationships:
        owner_node = sanitize_node_id(owner_id)
        child_node = sanitize_node_id(child_id)
        mermaid_lines.append(f"    {owner_node} --> {child_node}")

    return "\n".join(mermaid_lines)


def main():
    possible_kinds = get_possible_kinds()
    kinds_help_text = ", ".join(possible_kinds)
    parser = argparse.ArgumentParser(
        description="Recursively discover and diagram all K8s objects related to a Helm release.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("release_name", help="The name of the Helm release to diagram.")
    parser.add_argument("-n", "--namespace", default="apigee", help="The K8s namespace of the release (default: apigee).")
    parser.add_argument("--deep-discovery", action="store_true", help="Enable deep discovery to find all recursively owned resources.")
    parser.add_argument("--include-kinds", nargs='+', choices=possible_kinds, metavar='KIND', default=[], help=f"Only include these resource Kinds in the output. \nPossible values: {kinds_help_text}")
    parser.add_argument("--exclude-kinds", nargs='+', choices=possible_kinds, metavar='KIND', default=[], help=f"Exclude these resource Kinds from the output. \nPossible values: {kinds_help_text}")
    parser.add_argument("--md-format", action="store_true", help="Format output in a markdown code block for easy copy-pasting.")
    args = parser.parse_args()

    api_clients = _get_api_clients()

    if args.deep_discovery:
        print("Deep discovery enabled. Searching for all related objects.")
        all_related_objects = discover_full_hierarchy(api_clients, args.namespace, args.release_name)
    else:
        print("Deep discovery disabled. Searching for Helm-managed objects only.")
        all_related_objects = discover_helm_managed_objects(api_clients, args.namespace, args.release_name)

    if not all_related_objects:
        print("\n" + "="*70, file=sys.stderr)
        print(f"Error: No objects found for Helm release '{args.release_name}' in namespace '{args.namespace}'.", file=sys.stderr)
        sys.exit(1)

    print(f"\nDiscovery complete. Found a total of {len(all_related_objects)} related objects.")

    include_set = set(args.include_kinds)
    exclude_set = set(args.exclude_kinds)
    filtered_objects = []
    if not include_set and not exclude_set:
        print("No filters applied. Including all discovered objects.")
        filtered_objects = all_related_objects
    else:
        print("Applying filters to discovered objects...")
        for obj in all_related_objects:
            kind = get_object_kind(obj)
            
            should_include = True

            if include_set:
                if kind not in include_set:
                    should_include = False
            
            if should_include:
                if kind in exclude_set:
                    should_include = False

            if should_include:
                filtered_objects.append(obj)
        print(f"Filters applied. {len(filtered_objects)} objects remaining for diagram.")

    relationships = build_relationship_map(all_related_objects, filtered_objects, args.release_name, args.namespace)
    mermaid_output = generate_mermaid_diagram(relationships, args.release_name)

    if args.md_format:
        print(f"\n#### Release: {args.release_name} | Namespace: {args.namespace}")
        print("```mermaid")
        print(mermaid_output)
        print("```")
    else:
        print("\n" + "="*50)
        print("Mermaid Diagram Code (copy and paste this):")
        print("="*50 + "\n")
        print(mermaid_output)
        print("\n" + "="*50)
        print("You can render this diagram using online editors like https://mermaid.live")
        print("="*50)


if __name__ == "__main__":
    main()
