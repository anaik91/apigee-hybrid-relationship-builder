Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'dev'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 21 related objects.
Applying filters to discovered objects...
Filters applied. 21 objects remaining for diagram.
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

    ApigeeEnvironmentcicloudspannedevda008e1["ApigeeEnvironment/ci-cloud-spanne-dev-da008e1"]
    ConfigMapapigeesynchronizercicloudspadevdggroupconfib809b91["ConfigMap/apigee-synchronizer-ci-cloud-spa-dev-dggroupconfi-b809b91"]
    ConfigMapapigeesynchronizerdevaddonmap["ConfigMap/apigee-synchronizer-dev-add-on-map"]
    Secretapigeeruntimecicloudspannedevda008e1config74d732["Secret/apigee-runtime-ci-cloud-spanne-dev-da008e1-config-74d732"]
    Secretapigeesynchronizercicloudspannedevda008e1configd0d6a3["Secret/apigee-synchronizer-ci-cloud-spanne-dev-da008e1-config-d0d6a3"]
    ServiceAccountapigeesynchronizercicloudspannedevda008e1["ServiceAccount/apigee-synchronizer-ci-cloud-spanne-dev-da008e1"]
    Certificateapigeeruntimecicloudspannedevda008e1["Certificate/apigee-runtime-ci-cloud-spanne-dev-da008e1"]
    Certificateapigeesynchronizercicloudspannedevda008e1["Certificate/apigee-synchronizer-ci-cloud-spanne-dev-da008e1"]
    ApigeeDeploymentapigeeruntimecicloudspannedevda008e1["ApigeeDeployment/apigee-runtime-ci-cloud-spanne-dev-da008e1"]
    ApigeeDeploymentapigeesynchronizercicloudspannedevda008e1["ApigeeDeployment/apigee-synchronizer-ci-cloud-spanne-dev-da008e1"]
    ReplicaSetapigeeruntimecicloudspannedevda008e11150gxh0z["ReplicaSet/apigee-runtime-ci-cloud-spanne-dev-da008e1-1150-gxh0z"]
    Serviceapigeeruntimecicloudspannedevda008e1["Service/apigee-runtime-ci-cloud-spanne-dev-da008e1"]
    ReplicaSetapigeesynchronizercicloudspannedevda008e1115040ltr["ReplicaSet/apigee-synchronizer-ci-cloud-spanne-dev-da008e1-1150-40ltr"]
    Serviceapigeesynchronizercicloudspannedevda008e1["Service/apigee-synchronizer-ci-cloud-spanne-dev-da008e1"]
    Podapigeeruntimecicloudspannedevda008e11150gxh0znx4tr["Pod/apigee-runtime-ci-cloud-spanne-dev-da008e1-1150-gxh0z-nx4tr"]
    Podapigeesynchronizercicloudspannedevda008e1115040ltr2xqr7["Pod/apigee-synchronizer-ci-cloud-spanne-dev-da008e1-1150-40ltr2xqr7"]
    Podapigeesynchronizercicloudspannedevda008e1115040ltr42ltk["Pod/apigee-synchronizer-ci-cloud-spanne-dev-da008e1-1150-40ltr42ltk"]
    Podapigeesynchronizercicloudspannedevda008e1115040ltr57zn6["Pod/apigee-synchronizer-ci-cloud-spanne-dev-da008e1-1150-40ltr57zn6"]
    Podapigeesynchronizercicloudspannedevda008e1115040ltrq6z45["Pod/apigee-synchronizer-ci-cloud-spanne-dev-da008e1-1150-40ltrq6z45"]
    Podapigeesynchronizercicloudspannedevda008e1115040ltrq89h4["Pod/apigee-synchronizer-ci-cloud-spanne-dev-da008e1-1150-40ltrq89h4"]
    HelmReleasedev["Helm Release: dev"]
    Secretcicloudspannedevda008e1encryptionkeys["Secret/ci-cloud-spanne-dev-da008e1-encryption-keys"]

    class ApigeeEnvironmentcicloudspannedevda008e1 apigee_crd;
    class ConfigMapapigeesynchronizercicloudspadevdggroupconfib809b91 config;
    class ConfigMapapigeesynchronizerdevaddonmap config;
    class Secretapigeeruntimecicloudspannedevda008e1config74d732 config;
    class Secretapigeesynchronizercicloudspannedevda008e1configd0d6a3 config;
    class ServiceAccountapigeesynchronizercicloudspannedevda008e1 rbac;
    class Certificateapigeeruntimecicloudspannedevda008e1 cert_manager_crd;
    class Certificateapigeesynchronizercicloudspannedevda008e1 cert_manager_crd;
    class ApigeeDeploymentapigeeruntimecicloudspannedevda008e1 apigee_crd;
    class ApigeeDeploymentapigeesynchronizercicloudspannedevda008e1 apigee_crd;
    class ReplicaSetapigeeruntimecicloudspannedevda008e11150gxh0z workload;
    class Serviceapigeeruntimecicloudspannedevda008e1 network;
    class ReplicaSetapigeesynchronizercicloudspannedevda008e1115040ltr workload;
    class Serviceapigeesynchronizercicloudspannedevda008e1 network;
    class Podapigeeruntimecicloudspannedevda008e11150gxh0znx4tr workload;
    class Podapigeesynchronizercicloudspannedevda008e1115040ltr2xqr7 workload;
    class Podapigeesynchronizercicloudspannedevda008e1115040ltr42ltk workload;
    class Podapigeesynchronizercicloudspannedevda008e1115040ltr57zn6 workload;
    class Podapigeesynchronizercicloudspannedevda008e1115040ltrq6z45 workload;
    class Podapigeesynchronizercicloudspannedevda008e1115040ltrq89h4 workload;
    class HelmReleasedev helm;
    class Secretcicloudspannedevda008e1encryptionkeys config;

    ApigeeEnvironmentcicloudspannedevda008e1 --> ConfigMapapigeesynchronizercicloudspadevdggroupconfib809b91
    ApigeeEnvironmentcicloudspannedevda008e1 --> ConfigMapapigeesynchronizerdevaddonmap
    ApigeeEnvironmentcicloudspannedevda008e1 --> Secretapigeeruntimecicloudspannedevda008e1config74d732
    ApigeeEnvironmentcicloudspannedevda008e1 --> Secretapigeesynchronizercicloudspannedevda008e1configd0d6a3
    ApigeeEnvironmentcicloudspannedevda008e1 --> ServiceAccountapigeesynchronizercicloudspannedevda008e1
    ApigeeEnvironmentcicloudspannedevda008e1 --> Certificateapigeeruntimecicloudspannedevda008e1
    ApigeeEnvironmentcicloudspannedevda008e1 --> Certificateapigeesynchronizercicloudspannedevda008e1
    ApigeeEnvironmentcicloudspannedevda008e1 --> ApigeeDeploymentapigeeruntimecicloudspannedevda008e1
    ApigeeEnvironmentcicloudspannedevda008e1 --> ApigeeDeploymentapigeesynchronizercicloudspannedevda008e1
    ApigeeDeploymentapigeeruntimecicloudspannedevda008e1 --> ReplicaSetapigeeruntimecicloudspannedevda008e11150gxh0z
    ApigeeDeploymentapigeeruntimecicloudspannedevda008e1 --> Serviceapigeeruntimecicloudspannedevda008e1
    ApigeeDeploymentapigeesynchronizercicloudspannedevda008e1 --> ReplicaSetapigeesynchronizercicloudspannedevda008e1115040ltr
    ApigeeDeploymentapigeesynchronizercicloudspannedevda008e1 --> Serviceapigeesynchronizercicloudspannedevda008e1
    ReplicaSetapigeeruntimecicloudspannedevda008e11150gxh0z --> Podapigeeruntimecicloudspannedevda008e11150gxh0znx4tr
    ReplicaSetapigeesynchronizercicloudspannedevda008e1115040ltr --> Podapigeesynchronizercicloudspannedevda008e1115040ltr2xqr7
    ReplicaSetapigeesynchronizercicloudspannedevda008e1115040ltr --> Podapigeesynchronizercicloudspannedevda008e1115040ltr42ltk
    ReplicaSetapigeesynchronizercicloudspannedevda008e1115040ltr --> Podapigeesynchronizercicloudspannedevda008e1115040ltr57zn6
    ReplicaSetapigeesynchronizercicloudspannedevda008e1115040ltr --> Podapigeesynchronizercicloudspannedevda008e1115040ltrq6z45
    ReplicaSetapigeesynchronizercicloudspannedevda008e1115040ltr --> Podapigeesynchronizercicloudspannedevda008e1115040ltrq89h4
    HelmReleasedev --> Secretcicloudspannedevda008e1encryptionkeys
    HelmReleasedev --> ApigeeEnvironmentcicloudspannedevda008e1
```
