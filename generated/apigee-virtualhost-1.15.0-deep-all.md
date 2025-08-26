Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'apigee-virtualhost-test2'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 2 related objects.
No filters applied. Including all discovered objects.
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

    ApigeeRouteConfigapigeehybrid378710test2["ApigeeRouteConfig/apigee-hybrid-378710-test2"]
    ApigeeRouteapigeehybrid378710test20007196418["ApigeeRoute/apigee-hybrid-378710-test2-000-7196418"]
    HelmReleaseapigeevirtualhosttest2["Helm Release: apigee-virtualhost-test2"]

    class ApigeeRouteConfigapigeehybrid378710test2 apigee_crd;
    class ApigeeRouteapigeehybrid378710test20007196418 apigee_crd;
    class HelmReleaseapigeevirtualhosttest2 helm;

    ApigeeRouteConfigapigeehybrid378710test2 --> ApigeeRouteapigeehybrid378710test20007196418
    HelmReleaseapigeevirtualhosttest2 --> ApigeeRouteConfigapigeehybrid378710test2
```
