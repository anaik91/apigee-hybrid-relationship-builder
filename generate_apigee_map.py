import sys
import argparse
from collections import deque
from kubernetes import client, config

# --- Configuration ---
HELM_ANNOTATION_RELEASE_NAME = "meta.helm.sh/release-name"
HELM_ANNOTATION_RELEASE_NAMESPACE = "meta.helm.sh/release-namespace"

# Centralized list of all resource types to fetch for discovery
RESOURCE_FETCHERS = {
    "namespaced": [
        lambda api, n: api["v1"].list_namespaced_pod(n).items,
        lambda api, n: api["apps_v1"].list_namespaced_deployment(n).items,
        lambda api, n: api["apps_v1"].list_namespaced_replica_set(n).items,
        lambda api, n: api["apps_v1"].list_namespaced_stateful_set(n).items,
        lambda api, n: api["apps_v1"].list_namespaced_daemon_set(n).items,
        lambda api, n: api["v1"].list_namespaced_service(n).items,
        lambda api, n: api["v1"].list_namespaced_config_map(n).items,
        lambda api, n: api["v1"].list_namespaced_secret(n).items,
        lambda api, n: api["v1"].list_namespaced_service_account(n).items,
        lambda api, n: api["rbac_v1"].list_namespaced_role(n).items,
        lambda api, n: api["rbac_v1"].list_namespaced_role_binding(n).items,
        lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha2", n, "apigeeorganizations").get("items", []),
        lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha2", n, "apigeeenvironments").get("items", []),
        lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha3", n, "apigeedeployments").get("items", []),
        lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha1", n, "apigeeredis").get("items", []),
        lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha1", n, "apigeedatastores").get("items", []),
        lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha1", n, "apigeeissues").get("items", []),
        lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha1", n, "apigeerouteconfigs").get("items", []),
        lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha2", n, "apigeeroutes").get("items", []),
        lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha2", n, "apigeetelemetries").get("items", []),
        lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha1", n, "cassandradatareplications").get("items", []),
        lambda api, n: api["custom"].list_namespaced_custom_object("apigee.cloud.google.com", "v1alpha1", n, "secretrotations").get("items", []),
        lambda api, n: api["custom"].list_namespaced_custom_object("cert-manager.io", "v1", n, "certificates").get("items", []),
    ],
    "cluster": [
        lambda api: api["wh_v1"].list_mutating_webhook_configuration().items,
        lambda api: api["wh_v1"].list_validating_webhook_configuration().items,
        lambda api: api["rbac_v1"].list_cluster_role().items,
        lambda api: api["rbac_v1"].list_cluster_role_binding().items,
        lambda api: api["custom"].list_cluster_custom_object("cert-manager.io", "v1", "clusterissuers").get("items", []),
    ]
}


def _get_api_clients():
    """Helper to load kube config and initialize API clients."""
    try:
        config.load_kube_config()
        return {
            "v1": client.CoreV1Api(),
            "apps_v1": client.AppsV1Api(),
            "rbac_v1": client.RbacAuthorizationV1Api(),
            "custom": client.CustomObjectsApi(),
            "wh_v1" : client.AdmissionregistrationV1Api()
        }
    except Exception as e:
        print(f"Error: Could not configure Kubernetes client: {e}", file=sys.stderr)
        sys.exit(1)


def _fetch_all_potential_objects(api_clients, namespace):
    """Helper to fetch all defined resource types from the cluster."""
    all_potential_objects = []
    # Fetch namespaced resources
    for fetcher in RESOURCE_FETCHERS["namespaced"]:
        try:
            all_potential_objects.extend(fetcher(api_clients, namespace))
        except client.ApiException as e:
            if e.status != 404:
                print(f"Warning: Could not fetch a namespaced resource type: {e.reason}", file=sys.stderr)
    # Fetch cluster-wide resources
    for fetcher in RESOURCE_FETCHERS["cluster"]:
        try:
            all_potential_objects.extend(fetcher(api_clients))
        except client.ApiException as e:
            if e.status != 404:
                print(f"Warning: Could not fetch a cluster resource type: {e.reason}", file=sys.stderr)
    return all_potential_objects


def get_object_uid(k8s_object):
    is_dict = isinstance(k8s_object, dict)
    return k8s_object['metadata']['uid'] if is_dict else k8s_object.metadata.uid

def get_object_kind(k8s_object):
    if isinstance(k8s_object, dict): return k8s_object.get('kind', 'Unknown')
    kind = k8s_object.kind
    if kind: return kind
    class_name = type(k8s_object).__name__
    return class_name[2:] if class_name.startswith('V1') else class_name

def get_object_name(k8s_object):
    is_dict = isinstance(k8s_object, dict)
    return k8s_object['metadata']['name'] if is_dict else k8s_object.metadata.name
    
def get_object_spec(k8s_object):
    is_dict = isinstance(k8s_object, dict)
    return k8s_object.get('spec') if is_dict else getattr(k8s_object, 'spec', None)


### NEW: This function performs a shallow discovery, only finding objects
### with direct Helm annotations.
def discover_helm_managed_objects(api_clients, namespace, release_name):
    """
    Discovers only the objects directly managed by the specified Helm release.
    """
    print("Fetching all potential resources for shallow discovery...")
    all_potential_objects = _fetch_all_potential_objects(api_clients, namespace)
    
    print(f"Identifying objects directly managed by release '{release_name}'...")
    seed_objects = []
    for obj in all_potential_objects:
        is_dict = isinstance(obj, dict)
        metadata = obj['metadata'] if is_dict else obj.metadata
        annotations = metadata.get('annotations') if is_dict else metadata.annotations
        if annotations and (annotations.get(HELM_ANNOTATION_RELEASE_NAME) == release_name and
                           annotations.get(HELM_ANNOTATION_RELEASE_NAMESPACE) == namespace):
            seed_objects.append(obj)
            
    return seed_objects


def discover_full_hierarchy(api_clients, namespace, release_name):
    """
    Discovers the complete hierarchy of objects starting from a Helm release (deep discovery).
    """
    print("Fetching all potential resources for deep discovery...")
    all_potential_objects = _fetch_all_potential_objects(api_clients, namespace)
    
    # Step 1: Identify the initial 'seed' objects managed directly by Helm
    print(f"Identifying seed objects for release '{release_name}'...")
    seed_objects = []
    for obj in all_potential_objects:
        is_dict = isinstance(obj, dict)
        metadata = obj['metadata'] if is_dict else obj.metadata
        annotations = metadata.get('annotations') if is_dict else metadata.annotations
        if annotations and (annotations.get(HELM_ANNOTATION_RELEASE_NAME) == release_name and
                           annotations.get(HELM_ANNOTATION_RELEASE_NAMESPACE) == namespace):
            seed_objects.append(obj)

    if not seed_objects:
        return []

    # Step 2: Perform recursive discovery using a queue (Breadth-First Search)
    print("Starting recursive discovery from seed objects...")
    final_objects = {}
    discovery_queue = deque(seed_objects)
    processed_uids = set()

    while discovery_queue:
        parent_obj = discovery_queue.popleft()
        parent_uid = get_object_uid(parent_obj)
        if parent_uid in processed_uids: continue
        
        processed_uids.add(parent_uid)
        final_objects[parent_uid] = parent_obj

        for child_obj in all_potential_objects:
            child_uid = get_object_uid(child_obj)
            if child_uid in processed_uids: continue
            
            is_dict = isinstance(child_obj, dict)
            metadata = child_obj['metadata'] if is_dict else child_obj.metadata
            owner_refs = metadata.get('ownerReferences', []) if is_dict else (metadata.owner_references or [])
            
            for owner in owner_refs:
                owner_uid = owner.get('uid') if isinstance(owner, dict) else owner.uid
                if owner_uid == parent_uid:
                    discovery_queue.append(child_obj)
                    break

    return list(final_objects.values())


def build_relationship_map(objects, release_name, namespace):
    """
    Builds a map of parent-child relationships from a list of K8s objects.
    """
    print("Building relationship map...")
    relationships = []
    uid_to_node_id = {get_object_uid(obj): f"{get_object_kind(obj)}/{get_object_name(obj)}" for obj in objects}
    children_with_parents = set()

    for obj in objects:
        child_id = uid_to_node_id.get(get_object_uid(obj))
        if not child_id: continue

        parent_id = None
        is_dict = isinstance(obj, dict)
        metadata = obj['metadata'] if is_dict else obj.metadata
        owner_refs = metadata.get('ownerReferences') if is_dict else metadata.owner_references
        
        if owner_refs:
            owner_uid = owner_refs[0].get('uid') if isinstance(owner_refs[0], dict) else owner_refs[0].uid
            if owner_uid in uid_to_node_id:
                parent_id = uid_to_node_id[owner_uid]
                
        child_kind = get_object_kind(obj)
        if not parent_id and child_kind == 'ApigeeDeployment':
            spec = get_object_spec(obj)
            if spec and 'env' in spec:
                parent_id = f"ApigeeEnvironment/{spec['env']}"

        if parent_id:
            relationships.append((parent_id, child_id))
            children_with_parents.add(child_id)

    for obj in objects:
        child_id = uid_to_node_id.get(get_object_uid(obj))
        if not child_id or child_id in children_with_parents:
            continue

        is_dict = isinstance(obj, dict)
        metadata = obj['metadata'] if is_dict else obj.metadata
        annotations = metadata.get('annotations') if is_dict else metadata.annotations

        if annotations and (annotations.get(HELM_ANNOTATION_RELEASE_NAME) == release_name and
                           annotations.get(HELM_ANNOTATION_RELEASE_NAMESPACE) == namespace):
            parent_id = f'Helm Release: {release_name}'
            relationships.append((parent_id, child_id))
            children_with_parents.add(child_id)

    return relationships


def generate_mermaid_diagram(relationships, release_name):
    """
    Generates the Mermaid diagram from a list of parent-child relationships.
    """
    print("Generating Mermaid diagram...")
    declared_nodes = set()
    mermaid_lines = ["graph TD;"]
    
    mermaid_lines.append('    classDef helm fill:#f9f,stroke:#333,stroke-width:2px;')
    mermaid_lines.append('    classDef primitive fill:#d4edda,stroke:#155724,stroke-width:1px;')
    mermaid_lines.append('    classDef apigee_crd fill:#fff3cd,stroke:#856404,stroke-width:2px;')

    for owner_id, child_id in relationships:
        owner_node = "".join(filter(str.isalnum, owner_id))
        child_node = "".join(filter(str.isalnum, child_id))

        if owner_node not in declared_nodes:
            mermaid_lines.append(f'    {owner_node}["{owner_id}"]')
            declared_nodes.add(owner_node)
            if owner_id.startswith("Helm Release:"): mermaid_lines.append(f'    class {owner_node} helm;')
            elif owner_id.startswith("Apigee"): mermaid_lines.append(f'    class {owner_node} apigee_crd;')
            else: mermaid_lines.append(f'    class {owner_node} primitive;')

        if child_node not in declared_nodes:
            mermaid_lines.append(f'    {child_node}["{child_id}"]')
            declared_nodes.add(child_node)
            if child_id.startswith("Apigee"): mermaid_lines.append(f'    class {child_node} apigee_crd;')
            else: mermaid_lines.append(f'    class {child_node} primitive;')

        mermaid_lines.append(f"    {owner_node} --> {child_node}")

    return "\n".join(mermaid_lines)


def main():
    parser = argparse.ArgumentParser(
        description="Recursively discover and diagram all K8s objects related to a Helm release.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("release_name", help="The name of the Helm release to diagram.")
    parser.add_argument("-n", "--namespace", default="apigee", help="The K8s namespace of the release.")
    ### MODIFIED: Add the deep discovery flag
    parser.add_argument(
        "--deep-discovery",
        action="store_true",
        help="Enable deep discovery to find all recursively owned resources."
    )
    parser.add_argument(
        "--md-format",
        action="store_true",
        help="Enable deep discovery to find all recursively owned resources."
    )
    args = parser.parse_args()

    # Initialize K8s API clients once
    api_clients = _get_api_clients()
    
    ### MODIFIED: Choose discovery method based on the flag
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
    
    relationships = build_relationship_map(all_related_objects, args.release_name, args.namespace)
    mermaid_output = generate_mermaid_diagram(relationships, args.release_name)

    if args.md_format:
        print(f"#### Release {args.release_name} -> Namespace {args.namespace}")
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