# Kubernetes Helm Release Visualizer
This script is a command-line tool that discovers all Kubernetes resources associated with a specific Helm release and generates a Mermaid diagram to visualize their hierarchy and relationships.

It can perform two types of discovery:

1. **Shallow Discovery (Default):** Shows only the resources created directly by the Helm release.
2. **Deep Discovery:** Shows the Helm-managed resources and all the subsequent resources they create (e.g., a Deployment creating ReplicaSets, which in turn create Pods).

The generated diagram helps in understanding the entire footprint of a Helm chart, debugging ownership issues, and documenting your application's architecture in Kubernetes.

## Key Features
* Visualize Helm Releases: See exactly what components a Helm chart deploys.
* Toggleable Deep Discovery: Choose between a high-level overview or a detailed, recursive hierarchy.
* Intelligent Relationship Mapping: Correctly identifies parent-child relationships using Kubernetes ownerReferences.
* Custom Resource Definition (CRD) Support: Includes logic to find relationships for common CRDs like those from Apigee and cert-manager.
* Clear Visual Output: Generates a styled Mermaid diagram with distinct colors for the Helm release, CRDs, and standard Kubernetes resources.

## Example Diagram
The script outputs Mermaid graph definition code. When rendered by a tool like the Mermaid Live Editor, it produces a visual graph.

### Diagram Legend:
* Pink (#f9f): The Helm Release itself.
* Yellow (#fff3cd): Apigee Custom Resources (CRDs).
* Green (#d4edda): Standard Kubernetes resources (Deployments, Services, Pods, etc.).

## Prerequisites
Before you begin, ensure you have the following:
* Python 3.6+
* pip (Python package installer)
* A configured kubeconfig file: Your kubectl must be configured to point to the Kubernetes cluster you wish to inspect. You can test this with kubectl cluster-info.

## Installation
* Install dependencies: Open your terminal in the script's directory and run:
    ```bash
    pip install -r requirements.txt
    ```
## Usage
Run the script from your command line, providing the name of the Helm release you want to diagram.
Command Syntax

```bash
python generate_apigee_map.py <release_name> [options]
```
### Arguments
|Argument|Description|Required|	Default|
| -------- | ------- |------- |------- |
|release_name|The name of the Helm release to diagram.|Yes|N/A|
|-n, --namespace|The Kubernetes namespace where the release is located.|No|apigee
|--deep-discovery|A flag to enable deep, recursive discovery of all child/descendant objects.|No|Disabled|
|--include-kinds|Filter to only include these resource Kinds in the output|No|ApigeeDatastore, ApigeeDeployment, ApigeeEnvironment, ApigeeIssue, ApigeeOrganization, ApigeeRedis, ApigeeRoute, ApigeeRouteConfig, ApigeeTelemetry, CassandraDatareplication, Certificate, ClusterIssuer, ClusterRole, ClusterRoleBinding, ConfigMap, DaemonSet, Deployment, MutatingWebhookConfiguration, Pod, ReplicaSet, Role, RoleBinding, Secret, SecretRotation, Service, ServiceAccount, StatefulSet, ValidatingWebhookConfiguration|
|--exclude-kindsy|Filter to only exclude these resource Kinds in the output.|No|None|

## Examples
* Example 1: Shallow Discovery (Default)
    This command will find only the resources directly managed by the my-app Helm release in the production namespace.
    ```bash
    python generate_apigee_map.py my-app -n production
    ```
    The output will be a Mermaid diagram showing direct lines from "Helm Release: my-app" to the resources it created, like Deployments, Services, and ConfigMaps.

* Example 2: Deep Discovery
    This command will find all related resources for the apigee-runtime release in the default apigee namespace. It will trace the hierarchy from Deployments down to ReplicaSets and Pods.
    ```bash
    python generate_apigee_map.py apigee-runtime --deep-discovery
    ```
    The output will be a much more detailed diagram showing the full ownership chain.


* Example 3: Include certain kinds
    This command will find all related resources for the apigee-runtime release in the default apigee namespace. But will only include Deployment 
    ```bash
    python3 generate_apigee_map.py -n apigee operator --include-kinds Deployment 
    ```
    The output will only contain resources of kind : Deployment.

* Example 4: Exclude certain kinds
    This command will find all related resources for the apigee-runtime release in the default apigee namespace. But will exclude ClusterRole ClusterRoleBinding Role RoleBinding ServiceAccount 
    ```bash
    python3 generate_apigee_map.py -n apigee operator --exclude-kinds ClusterRole ClusterRoleBinding Role RoleBinding ServiceAccount 
    ```
    The output will not contain resources of kind : ClusterRole ClusterRoleBinding Role RoleBinding ServiceAccount.

## Rendering the Diagram
After running the script, it will print the Mermaid diagram code directly to your console.
1. Copy the entire block of code starting with graph TD;.
2. Paste it into a Mermaid-compatible renderer:
    * Online: The Mermaid Live Editor is the easiest option.
    * IDEs: Many editors like VS Code have extensions for rendering Mermaid diagrams (e.g., "Markdown Preview Mermaid Support").
    * Documentation: Platforms like GitHub and GitLab automatically render Mermaid syntax within Markdown files.