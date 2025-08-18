Deep discovery disabled. Searching for Helm-managed objects only.
Fetching all potential resources for shallow discovery...
Identifying objects directly managed by release 'apigee-hw'...

Discovery complete. Found a total of 8 related objects.
Applying filters to discovered objects...
Filters applied. 8 objects remaining for diagram.
Building relationship map...
Generating Mermaid diagram with color-coded kinds...

#### Release: apigee-hw | Namespace: apigee
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

    HelmReleaseapigeehw["Helm Release: apigee-hw"]
    Secretapigeeconnectagentapigeehw02a578bsvcaccount["Secret/apigee-connect-agent-apigee-hw-02a578b-svc-account"]
    Secretapigeehw02a578baxsalt["Secret/apigee-hw-02a578b-ax-salt"]
    Secretapigeehw02a578bdataencryption["Secret/apigee-hw-02a578b-data-encryption"]
    Secretapigeehw02a578bencryptionkeys["Secret/apigee-hw-02a578b-encryption-keys"]
    Secretapigeemartapigeehw02a578bsvcaccount["Secret/apigee-mart-apigee-hw-02a578b-svc-account"]
    Secretapigeeudcaapigeehw02a578bsvcaccount["Secret/apigee-udca-apigee-hw-02a578b-svc-account"]
    Secretapigeewatcherapigeehw02a578bsvcaccount["Secret/apigee-watcher-apigee-hw-02a578b-svc-account"]
    ApigeeOrganizationapigeehw02a578b["ApigeeOrganization/apigee-hw-02a578b"]

    class HelmReleaseapigeehw helm;
    class Secretapigeeconnectagentapigeehw02a578bsvcaccount config;
    class Secretapigeehw02a578baxsalt config;
    class Secretapigeehw02a578bdataencryption config;
    class Secretapigeehw02a578bencryptionkeys config;
    class Secretapigeemartapigeehw02a578bsvcaccount config;
    class Secretapigeeudcaapigeehw02a578bsvcaccount config;
    class Secretapigeewatcherapigeehw02a578bsvcaccount config;
    class ApigeeOrganizationapigeehw02a578b apigee_crd;

    HelmReleaseapigeehw --> Secretapigeeconnectagentapigeehw02a578bsvcaccount
    HelmReleaseapigeehw --> Secretapigeehw02a578baxsalt
    HelmReleaseapigeehw --> Secretapigeehw02a578bdataencryption
    HelmReleaseapigeehw --> Secretapigeehw02a578bencryptionkeys
    HelmReleaseapigeehw --> Secretapigeemartapigeehw02a578bsvcaccount
    HelmReleaseapigeehw --> Secretapigeeudcaapigeehw02a578bsvcaccount
    HelmReleaseapigeehw --> Secretapigeewatcherapigeehw02a578bsvcaccount
    HelmReleaseapigeehw --> ApigeeOrganizationapigeehw02a578b
```
