# Apigee Hybrid Helm Chart Dpeloyment Flow Sequence 

## Helm anatomy
```mermad
graph TD
    subgraph "A) Helm Chart ('my-helm-chart/')"
    
        direction LR
        ChartMeta["Chart.yaml<br/><i>(Metadata: name, version)</i>"]
        Values["values.yaml<br/><i>(Default Configuration)</i>"]
        Templates["templates/ Directory<br/><i>(K8s Manifest Templates)</i>"]
        
        subgraph " "
           direction TB
           T_Deploy["deployment.yaml<br/>spec:<br/>&nbsp;&nbsp;replicas: {{ .Values.replicaCount }}"]
           T_Svc["service.yaml<br/>spec:<br/>&nbsp;&nbsp;port: {{ .Values.service.port }}"]
        end
        Templates --> T_Deploy & T_Svc
    end

    subgraph "B) User's Configuration"
        UserValues["Custom Values<br/><i>(e.g., --set replicaCount=3)</i>"]
    end

    subgraph "C) The Helm Process"
        HelmCLI["<b>Helm Engine</b><br/><i>'helm install my-release ...'</i>"]
    end

    subgraph "D) The Result"
        Rendered["Rendered K8s Manifests<br/><i>(Final YAML)</i>"]
        K8sAPI["Kubernetes API Server"]
        
        subgraph "E) Running in Kubernetes Cluster (The 'Release')"
            direction LR
            Pod[Pod]
            Service[Service]
            Deployment[Deployment]
        end
    end

    %% Define the flow
    ChartMeta --> HelmCLI
    Values --> HelmCLI
    Templates --> HelmCLI
    UserValues --> HelmCLI

    HelmCLI -- Renders templates with values --> Rendered
    Rendered -- Sends to Kubernetes --> K8sAPI
    K8sAPI -- Creates Resources --> Deployment
    Deployment --> Pod
    K8sAPI --> Service
    
    %% Styling
    style HelmCLI fill:#0f9d58,stroke:#333,stroke-width:2px,color:#fff
    style K8sAPI fill:#326ce5,stroke:#333,stroke-width:2px,color:#fff
```

## Apigee Hybrid Helm sequnce
```mermaid
flowchart TD
    %% --- Style Definitions for different component types ---
    classDef prereq fill:#e6f2ff,stroke:#4a90e2,stroke-width:2px,font-weight:bold
    classDef operator fill:#fffbe6,stroke:#f5a623,stroke-width:2px,font-weight:bold
    classDef core fill:#e6fffa,stroke:#50e3c2,stroke-width:2px
    classDef runtime fill:#f2e6ff,stroke:#9013fe,stroke-width:2px

    %% --- Chart Structure ---

    %% 1. Prerequisite step
    A([Apply Apigee CRDs]):::prereq

    %% 2. Operator (Controller)
    B[apigee-operator]:::operator

    %% 3. Core singleton components
    C[apigee-datastore]:::core
    D[apigee-telemetry]:::core
    E[apigee-redis]:::core
    F[apigee-ingress-manager]:::core
    G[apigee-org]:::core

    %% 4. Repeatable runtime components
    H[[apigee-env]]:::runtime
    I[[apigee-virtualhost]]:::runtime

    A --> B --> C --> D --> E --> F --> G --> H --> I
```