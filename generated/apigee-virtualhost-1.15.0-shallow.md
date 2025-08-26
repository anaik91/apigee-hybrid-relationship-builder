Deep discovery disabled. Searching for Helm-managed objects only.
Fetching all potential resources for shallow discovery...
Identifying objects directly managed by release 'apigee-virtualhost-test2'...

Discovery complete. Found a total of 1 related objects.
Applying filters to discovered objects...
Filters applied. 1 objects remaining for diagram.
Building relationship map...
Generating Mermaid diagram with color-coded kinds...

#### Release: apigee-virtualhost-test2 | Namespace: apigee
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

    HelmReleaseapigeevirtualhosttest2["Helm Release: apigee-virtualhost-test2"]
    ApigeeRouteConfigapigeehybrid378710test2["ApigeeRouteConfig/apigee-hybrid-378710-test2"]

    class HelmReleaseapigeevirtualhosttest2 helm;
    class ApigeeRouteConfigapigeehybrid378710test2 apigee_crd;

    HelmReleaseapigeevirtualhosttest2 --> ApigeeRouteConfigapigeehybrid378710test2
```
