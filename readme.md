Kubernetes Helm Release Visualizer
This script is a command-line tool that discovers all Kubernetes resources associated with a specific Helm release and generates a Mermaid diagram to visualize their hierarchy and relationships.
It can perform two types of discovery:
Shallow Discovery (Default): Shows only the resources created directly by the Helm release.
Deep Discovery: Shows the Helm-managed resources and all the subsequent resources they create (e.g., a Deployment creating ReplicaSets, which in turn create Pods).
The generated diagram helps in understanding the entire footprint of a Helm chart, debugging ownership issues, and documenting your application's architecture in Kubernetes.
Key Features
Visualize Helm Releases: See exactly what components a Helm chart deploys.
Toggleable Deep Discovery: Choose between a high-level overview or a detailed, recursive hierarchy.
Intelligent Relationship Mapping: Correctly identifies parent-child relationships using Kubernetes ownerReferences.
Custom Resource Definition (CRD) Support: Includes logic to find relationships for common CRDs like those from Apigee and cert-manager.
Clear Visual Output: Generates a styled Mermaid diagram with distinct colors for the Helm release, CRDs, and standard Kubernetes resources.
Example Diagram
The script outputs Mermaid graph definition code. When rendered by a tool like the Mermaid Live Editor, it produces a visual graph.
Diagram Legend:
Pink (#f9f): The Helm Release itself.
Yellow (#fff3cd): Apigee Custom Resources (CRDs).
Green (#d4edda): Standard Kubernetes resources (Deployments, Services, Pods, etc.).
Prerequisites
Before you begin, ensure you have the following:
Python 3.6+
pip (Python package installer)
A configured kubeconfig file: Your kubectl must be configured to point to the Kubernetes cluster you wish to inspect. You can test this with kubectl cluster-info.
Installation
Download the script: Save the script to a file, for example, helm_visualizer.py.
Create requirements.txt: In the same directory as your script, create a file named requirements.txt with the following content:
code
Text
# Main client for interacting with the Kubernetes API
kubernetes
Install dependencies: Open your terminal in the script's directory and run:
code
Bash
pip install -r requirements.txt
Usage
Run the script from your command line, providing the name of the Helm release you want to diagram.
Command Syntax
code
Bash
python helm_visualizer.py <release_name> [options]
Arguments
Argument	Description	Required	Default
release_name	The name of the Helm release to diagram.	Yes	N/A
-n, --namespace	The Kubernetes namespace where the release is located.	No	apigee
--deep-discovery	A flag to enable deep, recursive discovery of all child/descendant objects.	No	Disabled
Examples
Example 1: Shallow Discovery (Default)
This command will find only the resources directly managed by the my-app Helm release in the production namespace.
code
Bash
python helm_visualizer.py my-app -n production
The output will be a Mermaid diagram showing direct lines from "Helm Release: my-app" to the resources it created, like Deployments, Services, and ConfigMaps.
Example 2: Deep Discovery
This command will find all related resources for the apigee-runtime release in the default apigee namespace. It will trace the hierarchy from Deployments down to ReplicaSets and Pods.
code
Bash
python helm_visualizer.py apigee-runtime --deep-discovery
The output will be a much more detailed diagram showing the full ownership chain.
Rendering the Diagram
After running the script, it will print the Mermaid diagram code directly to your console.
Copy the entire block of code starting with graph TD;.
Paste it into a Mermaid-compatible renderer:
Online: The Mermaid Live Editor is the easiest option.
IDEs: Many editors like VS Code have extensions for rendering Mermaid diagrams (e.g., "Markdown Preview Mermaid Support").
Documentation: Platforms like GitHub and GitLab automatically render Mermaid syntax within Markdown files.