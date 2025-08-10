Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'env-group-dev'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 3 related objects.
Filters applied. 3 objects remaining for diagram.
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

    ApigeeRouteConfigcicloudspannerc06ddev["ApigeeRouteConfig/ci-cloud-spanner-c06d-dev"]
    ApigeeRoutecicloudspannerc06ddev000e64b80a["ApigeeRoute/ci-cloud-spanner-c06d-dev-000-e64b80a"]
    HelmReleaseenvgroupdev["Helm Release: env-group-dev"]
    Secretcicloudspannerc06ddev["Secret/ci-cloud-spanner-c06d-dev"]

    class ApigeeRouteConfigcicloudspannerc06ddev apigee_crd;
    class ApigeeRoutecicloudspannerc06ddev000e64b80a apigee_crd;
    class HelmReleaseenvgroupdev helm;
    class Secretcicloudspannerc06ddev config;

    ApigeeRouteConfigcicloudspannerc06ddev --> ApigeeRoutecicloudspannerc06ddev000e64b80a
    HelmReleaseenvgroupdev --> Secretcicloudspannerc06ddev
    HelmReleaseenvgroupdev --> ApigeeRouteConfigcicloudspannerc06ddev
```
