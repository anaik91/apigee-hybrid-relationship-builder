Deep discovery disabled. Searching for Helm-managed objects only.
Fetching all potential resources for shallow discovery...
Identifying objects directly managed by release 'env-group-dev'...

Discovery complete. Found a total of 2 related objects.
No filters applied. Including all discovered objects.
Building relationship map...
Generating Mermaid diagram with color-coded kinds...

#### Release: env-group-dev | Namespace: apigee
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

    HelmReleaseenvgroupdev["Helm Release: env-group-dev"]
    Secretcicloudspannerc06ddev["Secret/ci-cloud-spanner-c06d-dev"]
    ApigeeRouteConfigcicloudspannerc06ddev["ApigeeRouteConfig/ci-cloud-spanner-c06d-dev"]

    class HelmReleaseenvgroupdev helm;
    class Secretcicloudspannerc06ddev config;
    class ApigeeRouteConfigcicloudspannerc06ddev apigee_crd;

    HelmReleaseenvgroupdev --> Secretcicloudspannerc06ddev
    HelmReleaseenvgroupdev --> ApigeeRouteConfigcicloudspannerc06ddev
```
