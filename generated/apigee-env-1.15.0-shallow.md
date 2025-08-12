Deep discovery disabled. Searching for Helm-managed objects only.
Fetching all potential resources for shallow discovery...
Identifying objects directly managed by release 'dev'...

Discovery complete. Found a total of 2 related objects.
Applying filters to discovered objects...
Filters applied. 2 objects remaining for diagram.
Building relationship map...
Generating Mermaid diagram with color-coded kinds...

#### Release: dev | Namespace: apigee
```mermaid
graph TD;
    classDef helm fill:#f9f,stroke:#333,stroke-width:2px,color:#000
    classDef workload fill:#cce5ff,stroke:#004085,stroke-width:1px,color:#000
    classDef network fill:#d4edda,stroke:#155724,stroke-width:1px,color:#000
    classDef config fill:#e2e3e5,stroke:#383d41,stroke-width:1px,color:#000
    classDef rbac fill:#f8d7da,stroke:#721c24,stroke-width:1px,color:#000
    classDef apigee_crd fill:#fff3cd,stroke:#856404,stroke-width:2px,color:#000
    classDef cert_manager_crd fill:#d1ecf1,stroke:#0c5460,stroke-width:2px,color:#000
    classDef webhook fill:#ddd,stroke:#333,stroke-width:2px,color:#000
    classDef default fill:#fff,stroke:#333,stroke-width:1px,color:#000

    HelmReleasedev["Helm Release: dev"]
    Secretcicloudspannedevda008e1encryptionkeys["Secret/ci-cloud-spanne-dev-da008e1-encryption-keys"]
    ApigeeEnvironmentcicloudspannedevda008e1["ApigeeEnvironment/ci-cloud-spanne-dev-da008e1"]

    class HelmReleasedev helm;
    class Secretcicloudspannedevda008e1encryptionkeys config;
    class ApigeeEnvironmentcicloudspannedevda008e1 apigee_crd;

    HelmReleasedev --> Secretcicloudspannedevda008e1encryptionkeys
    HelmReleasedev --> ApigeeEnvironmentcicloudspannedevda008e1
```
