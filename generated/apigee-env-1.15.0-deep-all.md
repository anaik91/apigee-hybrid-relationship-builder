Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'dev'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 22 related objects.
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

    ApigeeEnvironmentapigeehwdeve8f1e25["ApigeeEnvironment/apigee-hw-dev-e8f1e25"]
    ConfigMapapigeesynchronizerapigeehwdevdggroupconfi0cdf141["ConfigMap/apigee-synchronizer-apigee-hw-dev-dggroupconfi-0cdf141"]
    ConfigMapapigeesynchronizerdevaddonmap["ConfigMap/apigee-synchronizer-dev-add-on-map"]
    Secretapigeeruntimeapigeehwdeve8f1e25config9b8c53["Secret/apigee-runtime-apigee-hw-dev-e8f1e25-config-9b8c53"]
    Secretapigeesynchronizerapigeehwdeve8f1e25config74dd12["Secret/apigee-synchronizer-apigee-hw-dev-e8f1e25-config-74dd12"]
    ServiceAccountapigeesynchronizerapigeehwdeve8f1e25["ServiceAccount/apigee-synchronizer-apigee-hw-dev-e8f1e25"]
    Certificateapigeeruntimeapigeehwdeve8f1e25["Certificate/apigee-runtime-apigee-hw-dev-e8f1e25"]
    Certificateapigeesynchronizerapigeehwdeve8f1e25["Certificate/apigee-synchronizer-apigee-hw-dev-e8f1e25"]
    ApigeeDeploymentapigeeruntimeapigeehwdeve8f1e25["ApigeeDeployment/apigee-runtime-apigee-hw-dev-e8f1e25"]
    ApigeeDeploymentapigeesynchronizerapigeehwdeve8f1e25["ApigeeDeployment/apigee-synchronizer-apigee-hw-dev-e8f1e25"]
    V2HorizontalPodAutoscalerapigeeruntimeapigeehwdeve8f1e25115091gn6["V2HorizontalPodAutoscaler/apigee-runtime-apigee-hw-dev-e8f1e25-1150-91gn6"]
    ReplicaSetapigeeruntimeapigeehwdeve8f1e25115091gn6["ReplicaSet/apigee-runtime-apigee-hw-dev-e8f1e25-1150-91gn6"]
    Serviceapigeeruntimeapigeehwdeve8f1e25["Service/apigee-runtime-apigee-hw-dev-e8f1e25"]
    V2HorizontalPodAutoscalerapigeesynchronizerapigeehwdeve8f1e2511507qh6r["V2HorizontalPodAutoscaler/apigee-synchronizer-apigee-hw-dev-e8f1e25-1150-7qh6r"]
    ReplicaSetapigeesynchronizerapigeehwdeve8f1e2511507qh6r["ReplicaSet/apigee-synchronizer-apigee-hw-dev-e8f1e25-1150-7qh6r"]
    Serviceapigeesynchronizerapigeehwdeve8f1e25["Service/apigee-synchronizer-apigee-hw-dev-e8f1e25"]
    Podapigeeruntimeapigeehwdeve8f1e25115091gn62nfr9["Pod/apigee-runtime-apigee-hw-dev-e8f1e25-1150-91gn6-2nfr9"]
    Podapigeesynchronizerapigeehwdeve8f1e2511507qh6rmb4zd["Pod/apigee-synchronizer-apigee-hw-dev-e8f1e25-1150-7qh6r-mb4zd"]
    HelmReleasedev["Helm Release: dev"]
    Secretapigeehwdeve8f1e25encryptionkeys["Secret/apigee-hw-dev-e8f1e25-encryption-keys"]
    Secretapigeeruntimeapigeehwdeve8f1e25svcaccount["Secret/apigee-runtime-apigee-hw-dev-e8f1e25-svc-account"]
    Secretapigeesynchronizerapigeehwdeve8f1e25svcaccount["Secret/apigee-synchronizer-apigee-hw-dev-e8f1e25-svc-account"]
    Secretapigeeudcaapigeehwdeve8f1e25svcaccount["Secret/apigee-udca-apigee-hw-dev-e8f1e25-svc-account"]

    class ApigeeEnvironmentapigeehwdeve8f1e25 apigee_crd;
    class ConfigMapapigeesynchronizerapigeehwdevdggroupconfi0cdf141 config;
    class ConfigMapapigeesynchronizerdevaddonmap config;
    class Secretapigeeruntimeapigeehwdeve8f1e25config9b8c53 config;
    class Secretapigeesynchronizerapigeehwdeve8f1e25config74dd12 config;
    class ServiceAccountapigeesynchronizerapigeehwdeve8f1e25 rbac;
    class Certificateapigeeruntimeapigeehwdeve8f1e25 cert_manager_crd;
    class Certificateapigeesynchronizerapigeehwdeve8f1e25 cert_manager_crd;
    class ApigeeDeploymentapigeeruntimeapigeehwdeve8f1e25 apigee_crd;
    class ApigeeDeploymentapigeesynchronizerapigeehwdeve8f1e25 apigee_crd;
    class V2HorizontalPodAutoscalerapigeeruntimeapigeehwdeve8f1e25115091gn6 workload;
    class ReplicaSetapigeeruntimeapigeehwdeve8f1e25115091gn6 workload;
    class Serviceapigeeruntimeapigeehwdeve8f1e25 network;
    class V2HorizontalPodAutoscalerapigeesynchronizerapigeehwdeve8f1e2511507qh6r workload;
    class ReplicaSetapigeesynchronizerapigeehwdeve8f1e2511507qh6r workload;
    class Serviceapigeesynchronizerapigeehwdeve8f1e25 network;
    class Podapigeeruntimeapigeehwdeve8f1e25115091gn62nfr9 workload;
    class Podapigeesynchronizerapigeehwdeve8f1e2511507qh6rmb4zd workload;
    class HelmReleasedev helm;
    class Secretapigeehwdeve8f1e25encryptionkeys config;
    class Secretapigeeruntimeapigeehwdeve8f1e25svcaccount config;
    class Secretapigeesynchronizerapigeehwdeve8f1e25svcaccount config;
    class Secretapigeeudcaapigeehwdeve8f1e25svcaccount config;

    ApigeeEnvironmentapigeehwdeve8f1e25 --> ConfigMapapigeesynchronizerapigeehwdevdggroupconfi0cdf141
    ApigeeEnvironmentapigeehwdeve8f1e25 --> ConfigMapapigeesynchronizerdevaddonmap
    ApigeeEnvironmentapigeehwdeve8f1e25 --> Secretapigeeruntimeapigeehwdeve8f1e25config9b8c53
    ApigeeEnvironmentapigeehwdeve8f1e25 --> Secretapigeesynchronizerapigeehwdeve8f1e25config74dd12
    ApigeeEnvironmentapigeehwdeve8f1e25 --> ServiceAccountapigeesynchronizerapigeehwdeve8f1e25
    ApigeeEnvironmentapigeehwdeve8f1e25 --> Certificateapigeeruntimeapigeehwdeve8f1e25
    ApigeeEnvironmentapigeehwdeve8f1e25 --> Certificateapigeesynchronizerapigeehwdeve8f1e25
    ApigeeEnvironmentapigeehwdeve8f1e25 --> ApigeeDeploymentapigeeruntimeapigeehwdeve8f1e25
    ApigeeEnvironmentapigeehwdeve8f1e25 --> ApigeeDeploymentapigeesynchronizerapigeehwdeve8f1e25
    ApigeeDeploymentapigeeruntimeapigeehwdeve8f1e25 --> V2HorizontalPodAutoscalerapigeeruntimeapigeehwdeve8f1e25115091gn6
    ApigeeDeploymentapigeeruntimeapigeehwdeve8f1e25 --> ReplicaSetapigeeruntimeapigeehwdeve8f1e25115091gn6
    ApigeeDeploymentapigeeruntimeapigeehwdeve8f1e25 --> Serviceapigeeruntimeapigeehwdeve8f1e25
    ApigeeDeploymentapigeesynchronizerapigeehwdeve8f1e25 --> V2HorizontalPodAutoscalerapigeesynchronizerapigeehwdeve8f1e2511507qh6r
    ApigeeDeploymentapigeesynchronizerapigeehwdeve8f1e25 --> ReplicaSetapigeesynchronizerapigeehwdeve8f1e2511507qh6r
    ApigeeDeploymentapigeesynchronizerapigeehwdeve8f1e25 --> Serviceapigeesynchronizerapigeehwdeve8f1e25
    ReplicaSetapigeeruntimeapigeehwdeve8f1e25115091gn6 --> Podapigeeruntimeapigeehwdeve8f1e25115091gn62nfr9
    ReplicaSetapigeesynchronizerapigeehwdeve8f1e2511507qh6r --> Podapigeesynchronizerapigeehwdeve8f1e2511507qh6rmb4zd
    HelmReleasedev --> Secretapigeehwdeve8f1e25encryptionkeys
    HelmReleasedev --> Secretapigeeruntimeapigeehwdeve8f1e25svcaccount
    HelmReleasedev --> Secretapigeesynchronizerapigeehwdeve8f1e25svcaccount
    HelmReleasedev --> Secretapigeeudcaapigeehwdeve8f1e25svcaccount
    HelmReleasedev --> ApigeeEnvironmentapigeehwdeve8f1e25
```
