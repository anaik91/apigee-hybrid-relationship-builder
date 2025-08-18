Deep discovery disabled. Searching for Helm-managed objects only.
Fetching all potential resources for shallow discovery...
Identifying objects directly managed by release 'dev'...

Discovery complete. Found a total of 5 related objects.
No filters applied. Including all discovered objects.
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
    Secretapigeehwdeve8f1e25encryptionkeys["Secret/apigee-hw-dev-e8f1e25-encryption-keys"]
    Secretapigeeruntimeapigeehwdeve8f1e25svcaccount["Secret/apigee-runtime-apigee-hw-dev-e8f1e25-svc-account"]
    Secretapigeesynchronizerapigeehwdeve8f1e25svcaccount["Secret/apigee-synchronizer-apigee-hw-dev-e8f1e25-svc-account"]
    Secretapigeeudcaapigeehwdeve8f1e25svcaccount["Secret/apigee-udca-apigee-hw-dev-e8f1e25-svc-account"]
    ApigeeEnvironmentapigeehwdeve8f1e25["ApigeeEnvironment/apigee-hw-dev-e8f1e25"]

    class HelmReleasedev helm;
    class Secretapigeehwdeve8f1e25encryptionkeys config;
    class Secretapigeeruntimeapigeehwdeve8f1e25svcaccount config;
    class Secretapigeesynchronizerapigeehwdeve8f1e25svcaccount config;
    class Secretapigeeudcaapigeehwdeve8f1e25svcaccount config;
    class ApigeeEnvironmentapigeehwdeve8f1e25 apigee_crd;

    HelmReleasedev --> Secretapigeehwdeve8f1e25encryptionkeys
    HelmReleasedev --> Secretapigeeruntimeapigeehwdeve8f1e25svcaccount
    HelmReleasedev --> Secretapigeesynchronizerapigeehwdeve8f1e25svcaccount
    HelmReleasedev --> Secretapigeeudcaapigeehwdeve8f1e25svcaccount
    HelmReleasedev --> ApigeeEnvironmentapigeehwdeve8f1e25
```
