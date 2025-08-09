Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'env-group-dev'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 3 related objects.
Building relationship map...
Generating Mermaid diagram...
#### Release env-group-dev -> Namespace apigee
```mermaid
graph TD;
    classDef helm fill:#f9f,stroke:#333,stroke-width:2px;
    classDef primitive fill:#d4edda,stroke:#155724,stroke-width:1px;
    classDef apigee_crd fill:#fff3cd,stroke:#856404,stroke-width:2px;
    ApigeeRouteConfigcicloudspannerc06ddev["ApigeeRouteConfig/ci-cloud-spanner-c06d-dev"]
    class ApigeeRouteConfigcicloudspannerc06ddev apigee_crd;
    ApigeeRoutecicloudspannerc06ddev000e64b80a["ApigeeRoute/ci-cloud-spanner-c06d-dev-000-e64b80a"]
    class ApigeeRoutecicloudspannerc06ddev000e64b80a apigee_crd;
    ApigeeRouteConfigcicloudspannerc06ddev --> ApigeeRoutecicloudspannerc06ddev000e64b80a
    HelmReleaseenvgroupdev["Helm Release: env-group-dev"]
    class HelmReleaseenvgroupdev helm;
    Secretcicloudspannerc06ddev["Secret/ci-cloud-spanner-c06d-dev"]
    class Secretcicloudspannerc06ddev primitive;
    HelmReleaseenvgroupdev --> Secretcicloudspannerc06ddev
    HelmReleaseenvgroupdev --> ApigeeRouteConfigcicloudspannerc06ddev
```
