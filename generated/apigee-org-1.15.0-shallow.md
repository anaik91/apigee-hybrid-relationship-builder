Deep discovery disabled. Searching for Helm-managed objects only.
Fetching all potential resources for shallow discovery...
Identifying objects directly managed by release 'ci-cloud-spanner-c06d'...

Discovery complete. Found a total of 6 related objects.
Applying filters to discovered objects...
Filters applied. 6 objects remaining for diagram.
Building relationship map...
Generating Mermaid diagram with color-coded kinds...

#### Release: ci-cloud-spanner-c06d | Namespace: apigee
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

    HelmReleasecicloudspannerc06d["Helm Release: ci-cloud-spanner-c06d"]
    Secretcicloudspanne660f3fbaxsalt["Secret/ci-cloud-spanne-660f3fb-ax-salt"]
    Secretcicloudspanne660f3fbdataencryption["Secret/ci-cloud-spanne-660f3fb-data-encryption"]
    Secretcicloudspanne660f3fbencryptionkeys["Secret/ci-cloud-spanne-660f3fb-encryption-keys"]
    Certificateapigeeingressgatewayinternalchainingcicloudspanne660f3fb["Certificate/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-660f3fb"]
    ApigeeOrganizationcicloudspanne660f3fb["ApigeeOrganization/ci-cloud-spanne-660f3fb"]
    ApigeeRouteapigeeingressgatewayinternalchainingcicloudspanne660f3fb["ApigeeRoute/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-660f3fb"]

    class HelmReleasecicloudspannerc06d helm;
    class Secretcicloudspanne660f3fbaxsalt config;
    class Secretcicloudspanne660f3fbdataencryption config;
    class Secretcicloudspanne660f3fbencryptionkeys config;
    class Certificateapigeeingressgatewayinternalchainingcicloudspanne660f3fb cert_manager_crd;
    class ApigeeOrganizationcicloudspanne660f3fb apigee_crd;
    class ApigeeRouteapigeeingressgatewayinternalchainingcicloudspanne660f3fb apigee_crd;

    HelmReleasecicloudspannerc06d --> Secretcicloudspanne660f3fbaxsalt
    HelmReleasecicloudspannerc06d --> Secretcicloudspanne660f3fbdataencryption
    HelmReleasecicloudspannerc06d --> Secretcicloudspanne660f3fbencryptionkeys
    HelmReleasecicloudspannerc06d --> Certificateapigeeingressgatewayinternalchainingcicloudspanne660f3fb
    HelmReleasecicloudspannerc06d --> ApigeeOrganizationcicloudspanne660f3fb
    HelmReleasecicloudspannerc06d --> ApigeeRouteapigeeingressgatewayinternalchainingcicloudspanne660f3fb
```
