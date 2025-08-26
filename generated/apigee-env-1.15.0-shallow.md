Deep discovery disabled. Searching for Helm-managed objects only.
Fetching all potential resources for shallow discovery...
Identifying objects directly managed by release 'apigee-env-test2'...

Discovery complete. Found a total of 2 related objects.
Applying filters to discovered objects...
Filters applied. 2 objects remaining for diagram.
Building relationship map...
Generating Mermaid diagram with color-coded kinds...

#### Release: apigee-env-test2 | Namespace: apigee
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

    HelmReleaseapigeeenvtest2["Helm Release: apigee-env-test2"]
    Secretapigeehybrid3test25a04239encryptionkeys["Secret/apigee-hybrid-3-test2-5a04239-encryption-keys"]
    ApigeeEnvironmentapigeehybrid3test25a04239["ApigeeEnvironment/apigee-hybrid-3-test2-5a04239"]

    class HelmReleaseapigeeenvtest2 helm;
    class Secretapigeehybrid3test25a04239encryptionkeys config;
    class ApigeeEnvironmentapigeehybrid3test25a04239 apigee_crd;

    HelmReleaseapigeeenvtest2 --> Secretapigeehybrid3test25a04239encryptionkeys
    HelmReleaseapigeeenvtest2 --> ApigeeEnvironmentapigeehybrid3test25a04239
```
