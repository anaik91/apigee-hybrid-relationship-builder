Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'group-a'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 3 related objects.
Applying filters to discovered objects...
Filters applied. 3 objects remaining for diagram.
Building relationship map...
Generating Mermaid diagram with color-coded kinds...

#### Release: group-a | Namespace: apigee
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

    ApigeeRouteConfigapigeehwgroupa["ApigeeRouteConfig/apigee-hw-group-a"]
    ApigeeRouteapigeehwgroupa0004df0e43["ApigeeRoute/apigee-hw-group-a-000-4df0e43"]
    HelmReleasegroupa["Helm Release: group-a"]
    Secretapigeehwgroupa["Secret/apigee-hw-group-a"]

    class ApigeeRouteConfigapigeehwgroupa apigee_crd;
    class ApigeeRouteapigeehwgroupa0004df0e43 apigee_crd;
    class HelmReleasegroupa helm;
    class Secretapigeehwgroupa config;

    ApigeeRouteConfigapigeehwgroupa --> ApigeeRouteapigeehwgroupa0004df0e43
    HelmReleasegroupa --> Secretapigeehwgroupa
    HelmReleasegroupa --> ApigeeRouteConfigapigeehwgroupa
```
