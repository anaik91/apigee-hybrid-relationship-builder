Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'apigee-env-test2'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 19 related objects.
No filters applied. Including all discovered objects.
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

    ApigeeEnvironmentapigeehybrid3test25a04239["ApigeeEnvironment/apigee-hybrid-3-test2-5a04239"]
    ConfigMapapigeesynchronizerapigeehybritest2dggroupconfie61fb5a["ConfigMap/apigee-synchronizer-apigee-hybri-test2-dggroupconfi-e61fb5a"]
    ConfigMapapigeesynchronizertest2addonmap["ConfigMap/apigee-synchronizer-test2-add-on-map"]
    Secretapigeeruntimeapigeehybrid3test25a04239config7435d7["Secret/apigee-runtime-apigee-hybrid-3-test2-5a04239-config-7435d7"]
    Secretapigeesynchronizerapigeehybrid3test25a04239config93907f["Secret/apigee-synchronizer-apigee-hybrid-3-test2-5a04239-config-93907f"]
    ServiceAccountapigeesynchronizerapigeehybrid3test25a04239["ServiceAccount/apigee-synchronizer-apigee-hybrid-3-test2-5a04239"]
    Certificateapigeeruntimeapigeehybrid3test25a04239["Certificate/apigee-runtime-apigee-hybrid-3-test2-5a04239"]
    Certificateapigeesynchronizerapigeehybrid3test25a04239["Certificate/apigee-synchronizer-apigee-hybrid-3-test2-5a04239"]
    ApigeeDeploymentapigeeruntimeapigeehybrid3test25a04239["ApigeeDeployment/apigee-runtime-apigee-hybrid-3-test2-5a04239"]
    ApigeeDeploymentapigeesynchronizerapigeehybrid3test25a04239["ApigeeDeployment/apigee-synchronizer-apigee-hybrid-3-test2-5a04239"]
    V2HorizontalPodAutoscalerapigeeruntimeapigeehybrid3test25a04239115023760["V2HorizontalPodAutoscaler/apigee-runtime-apigee-hybrid-3-test2-5a04239-1150-23760"]
    ReplicaSetapigeeruntimeapigeehybrid3test25a04239115023760["ReplicaSet/apigee-runtime-apigee-hybrid-3-test2-5a04239-1150-23760"]
    Serviceapigeeruntimeapigeehybrid3test25a04239["Service/apigee-runtime-apigee-hybrid-3-test2-5a04239"]
    V2HorizontalPodAutoscalerapigeesynchronizerapigeehybrid3test25a042391150955qa["V2HorizontalPodAutoscaler/apigee-synchronizer-apigee-hybrid-3-test2-5a04239-1150-955qa"]
    ReplicaSetapigeesynchronizerapigeehybrid3test25a042391150955qa["ReplicaSet/apigee-synchronizer-apigee-hybrid-3-test2-5a04239-1150-955qa"]
    Serviceapigeesynchronizerapigeehybrid3test25a04239["Service/apigee-synchronizer-apigee-hybrid-3-test2-5a04239"]
    Podapigeeruntimeapigeehybrid3test25a042391150237606mvtv["Pod/apigee-runtime-apigee-hybrid-3-test2-5a04239-1150-23760-6mvtv"]
    Podapigeesynchronizerapigeehybrid3test25a042391150955tplx8["Pod/apigee-synchronizer-apigee-hybrid-3-test2-5a04239-1150-955tplx8"]
    HelmReleaseapigeeenvtest2["Helm Release: apigee-env-test2"]
    Secretapigeehybrid3test25a04239encryptionkeys["Secret/apigee-hybrid-3-test2-5a04239-encryption-keys"]

    class ApigeeEnvironmentapigeehybrid3test25a04239 apigee_crd;
    class ConfigMapapigeesynchronizerapigeehybritest2dggroupconfie61fb5a config;
    class ConfigMapapigeesynchronizertest2addonmap config;
    class Secretapigeeruntimeapigeehybrid3test25a04239config7435d7 config;
    class Secretapigeesynchronizerapigeehybrid3test25a04239config93907f config;
    class ServiceAccountapigeesynchronizerapigeehybrid3test25a04239 rbac;
    class Certificateapigeeruntimeapigeehybrid3test25a04239 cert_manager_crd;
    class Certificateapigeesynchronizerapigeehybrid3test25a04239 cert_manager_crd;
    class ApigeeDeploymentapigeeruntimeapigeehybrid3test25a04239 apigee_crd;
    class ApigeeDeploymentapigeesynchronizerapigeehybrid3test25a04239 apigee_crd;
    class V2HorizontalPodAutoscalerapigeeruntimeapigeehybrid3test25a04239115023760 workload;
    class ReplicaSetapigeeruntimeapigeehybrid3test25a04239115023760 workload;
    class Serviceapigeeruntimeapigeehybrid3test25a04239 network;
    class V2HorizontalPodAutoscalerapigeesynchronizerapigeehybrid3test25a042391150955qa workload;
    class ReplicaSetapigeesynchronizerapigeehybrid3test25a042391150955qa workload;
    class Serviceapigeesynchronizerapigeehybrid3test25a04239 network;
    class Podapigeeruntimeapigeehybrid3test25a042391150237606mvtv workload;
    class Podapigeesynchronizerapigeehybrid3test25a042391150955tplx8 workload;
    class HelmReleaseapigeeenvtest2 helm;
    class Secretapigeehybrid3test25a04239encryptionkeys config;

    ApigeeEnvironmentapigeehybrid3test25a04239 --> ConfigMapapigeesynchronizerapigeehybritest2dggroupconfie61fb5a
    ApigeeEnvironmentapigeehybrid3test25a04239 --> ConfigMapapigeesynchronizertest2addonmap
    ApigeeEnvironmentapigeehybrid3test25a04239 --> Secretapigeeruntimeapigeehybrid3test25a04239config7435d7
    ApigeeEnvironmentapigeehybrid3test25a04239 --> Secretapigeesynchronizerapigeehybrid3test25a04239config93907f
    ApigeeEnvironmentapigeehybrid3test25a04239 --> ServiceAccountapigeesynchronizerapigeehybrid3test25a04239
    ApigeeEnvironmentapigeehybrid3test25a04239 --> Certificateapigeeruntimeapigeehybrid3test25a04239
    ApigeeEnvironmentapigeehybrid3test25a04239 --> Certificateapigeesynchronizerapigeehybrid3test25a04239
    ApigeeEnvironmentapigeehybrid3test25a04239 --> ApigeeDeploymentapigeeruntimeapigeehybrid3test25a04239
    ApigeeEnvironmentapigeehybrid3test25a04239 --> ApigeeDeploymentapigeesynchronizerapigeehybrid3test25a04239
    ApigeeDeploymentapigeeruntimeapigeehybrid3test25a04239 --> V2HorizontalPodAutoscalerapigeeruntimeapigeehybrid3test25a04239115023760
    ApigeeDeploymentapigeeruntimeapigeehybrid3test25a04239 --> ReplicaSetapigeeruntimeapigeehybrid3test25a04239115023760
    ApigeeDeploymentapigeeruntimeapigeehybrid3test25a04239 --> Serviceapigeeruntimeapigeehybrid3test25a04239
    ApigeeDeploymentapigeesynchronizerapigeehybrid3test25a04239 --> V2HorizontalPodAutoscalerapigeesynchronizerapigeehybrid3test25a042391150955qa
    ApigeeDeploymentapigeesynchronizerapigeehybrid3test25a04239 --> ReplicaSetapigeesynchronizerapigeehybrid3test25a042391150955qa
    ApigeeDeploymentapigeesynchronizerapigeehybrid3test25a04239 --> Serviceapigeesynchronizerapigeehybrid3test25a04239
    ReplicaSetapigeeruntimeapigeehybrid3test25a04239115023760 --> Podapigeeruntimeapigeehybrid3test25a042391150237606mvtv
    ReplicaSetapigeesynchronizerapigeehybrid3test25a042391150955qa --> Podapigeesynchronizerapigeehybrid3test25a042391150955tplx8
    HelmReleaseapigeeenvtest2 --> Secretapigeehybrid3test25a04239encryptionkeys
    HelmReleaseapigeeenvtest2 --> ApigeeEnvironmentapigeehybrid3test25a04239
```
