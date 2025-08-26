Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'telemetry'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 37 related objects.
Applying filters to discovered objects...
Filters applied. 35 objects remaining for diagram.
Building relationship map...
Generating Mermaid diagram with color-coded kinds...

#### Release: telemetry | Namespace: apigee
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

    ApigeeTelemetryapigeetelemetry["ApigeeTelemetry/apigee-telemetry"]
    DaemonSetapigeeloggerapigeetelemetry["DaemonSet/apigee-logger-apigee-telemetry"]
    ConfigMapapigeeloggerapigeetelemetry["ConfigMap/apigee-logger-apigee-telemetry"]
    ConfigMapapigeemetricsadapterapigeetelemetry["ConfigMap/apigee-metrics-adapter-apigee-telemetry"]
    ConfigMapapigeemetricsapigeetelemetryapp["ConfigMap/apigee-metrics-apigee-telemetry-app"]
    ConfigMapapigeeopentelemetrycollectorapigeetelemetry["ConfigMap/apigee-open-telemetry-collector-apigee-telemetry"]
    ServiceAccountapigeeloggerapigeetelemetry["ServiceAccount/apigee-logger-apigee-telemetry"]
    ServiceAccountapigeemetricsapigeetelemetry["ServiceAccount/apigee-metrics-apigee-telemetry"]
    ServiceAccountapigeeopentelemetrycollectorapigeetelemetry["ServiceAccount/apigee-open-telemetry-collector-apigee-telemetry"]
    Certificateapigeemetricsadapterapigeetelemetry["Certificate/apigee-metrics-adapter-apigee-telemetry"]
    ApigeeDeploymentapigeemetricsadapterapigeetelemetry["ApigeeDeployment/apigee-metrics-adapter-apigee-telemetry"]
    ApigeeDeploymentapigeemetricsapigeetelemetryapp["ApigeeDeployment/apigee-metrics-apigee-telemetry-app"]
    ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry["ApigeeDeployment/apigee-open-telemetry-collector-apigee-telemetry"]
    APIServicev1beta1custommetricsk8sio["APIService/v1beta1.custom.metrics.k8s.io"]
    Podapigeeloggerapigeetelemetry4dhzk["Pod/apigee-logger-apigee-telemetry-4dhzk"]
    Podapigeeloggerapigeetelemetry69nbt["Pod/apigee-logger-apigee-telemetry-69nbt"]
    Podapigeeloggerapigeetelemetry7xjfs["Pod/apigee-logger-apigee-telemetry-7xjfs"]
    Podapigeeloggerapigeetelemetrylbcpv["Pod/apigee-logger-apigee-telemetry-lbcpv"]
    Podapigeeloggerapigeetelemetrypfn2z["Pod/apigee-logger-apigee-telemetry-pfn2z"]
    Podapigeeloggerapigeetelemetryv9srb["Pod/apigee-logger-apigee-telemetry-v9srb"]
    V2HorizontalPodAutoscalerapigeemetricsadapterapigeetelemetry11509fjy0["V2HorizontalPodAutoscaler/apigee-metrics-adapter-apigee-telemetry-1150-9fjy0"]
    ReplicaSetapigeemetricsadapterapigeetelemetry11509fjy0["ReplicaSet/apigee-metrics-adapter-apigee-telemetry-1150-9fjy0"]
    Serviceapigeemetricsadapterapigeetelemetry["Service/apigee-metrics-adapter-apigee-telemetry"]
    V2HorizontalPodAutoscalerapigeemetricsapigeetelemetryapp115070qcv["V2HorizontalPodAutoscaler/apigee-metrics-apigee-telemetry-app-1150-70qcv"]
    ReplicaSetapigeemetricsapigeetelemetryapp115070qcv["ReplicaSet/apigee-metrics-apigee-telemetry-app-1150-70qcv"]
    Serviceapigeemetricsapigeetelemetryapp["Service/apigee-metrics-apigee-telemetry-app"]
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry["DaemonSet/apigee-open-telemetry-collector-apigee-telemetry"]
    Podapigeemetricsadapterapigeetelemetry11509fjy0slzn9["Pod/apigee-metrics-adapter-apigee-telemetry-1150-9fjy0-slzn9"]
    Podapigeemetricsapigeetelemetryapp115070qcv2xrjz["Pod/apigee-metrics-apigee-telemetry-app-1150-70qcv-2xrjz"]
    Podapigeeopentelemetrycollectorapigeetelemetry45jgc["Pod/apigee-open-telemetry-collector-apigee-telemetry-45jgc"]
    Podapigeeopentelemetrycollectorapigeetelemetry9jd85["Pod/apigee-open-telemetry-collector-apigee-telemetry-9jd85"]
    Podapigeeopentelemetrycollectorapigeetelemetrybg6xp["Pod/apigee-open-telemetry-collector-apigee-telemetry-bg6xp"]
    Podapigeeopentelemetrycollectorapigeetelemetryfn8lc["Pod/apigee-open-telemetry-collector-apigee-telemetry-fn8lc"]
    Podapigeeopentelemetrycollectorapigeetelemetryh99tk["Pod/apigee-open-telemetry-collector-apigee-telemetry-h99tk"]
    Podapigeeopentelemetrycollectorapigeetelemetryk6ls5["Pod/apigee-open-telemetry-collector-apigee-telemetry-k6ls5"]
    HelmReleasetelemetry["Helm Release: telemetry"]

    class ApigeeTelemetryapigeetelemetry apigee_crd;
    class DaemonSetapigeeloggerapigeetelemetry workload;
    class ConfigMapapigeeloggerapigeetelemetry config;
    class ConfigMapapigeemetricsadapterapigeetelemetry config;
    class ConfigMapapigeemetricsapigeetelemetryapp config;
    class ConfigMapapigeeopentelemetrycollectorapigeetelemetry config;
    class ServiceAccountapigeeloggerapigeetelemetry rbac;
    class ServiceAccountapigeemetricsapigeetelemetry rbac;
    class ServiceAccountapigeeopentelemetrycollectorapigeetelemetry rbac;
    class Certificateapigeemetricsadapterapigeetelemetry cert_manager_crd;
    class ApigeeDeploymentapigeemetricsadapterapigeetelemetry apigee_crd;
    class ApigeeDeploymentapigeemetricsapigeetelemetryapp apigee_crd;
    class ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry apigee_crd;
    class APIServicev1beta1custommetricsk8sio webhook;
    class Podapigeeloggerapigeetelemetry4dhzk workload;
    class Podapigeeloggerapigeetelemetry69nbt workload;
    class Podapigeeloggerapigeetelemetry7xjfs workload;
    class Podapigeeloggerapigeetelemetrylbcpv workload;
    class Podapigeeloggerapigeetelemetrypfn2z workload;
    class Podapigeeloggerapigeetelemetryv9srb workload;
    class V2HorizontalPodAutoscalerapigeemetricsadapterapigeetelemetry11509fjy0 workload;
    class ReplicaSetapigeemetricsadapterapigeetelemetry11509fjy0 workload;
    class Serviceapigeemetricsadapterapigeetelemetry network;
    class V2HorizontalPodAutoscalerapigeemetricsapigeetelemetryapp115070qcv workload;
    class ReplicaSetapigeemetricsapigeetelemetryapp115070qcv workload;
    class Serviceapigeemetricsapigeetelemetryapp network;
    class DaemonSetapigeeopentelemetrycollectorapigeetelemetry workload;
    class Podapigeemetricsadapterapigeetelemetry11509fjy0slzn9 workload;
    class Podapigeemetricsapigeetelemetryapp115070qcv2xrjz workload;
    class Podapigeeopentelemetrycollectorapigeetelemetry45jgc workload;
    class Podapigeeopentelemetrycollectorapigeetelemetry9jd85 workload;
    class Podapigeeopentelemetrycollectorapigeetelemetrybg6xp workload;
    class Podapigeeopentelemetrycollectorapigeetelemetryfn8lc workload;
    class Podapigeeopentelemetrycollectorapigeetelemetryh99tk workload;
    class Podapigeeopentelemetrycollectorapigeetelemetryk6ls5 workload;
    class HelmReleasetelemetry helm;

    ApigeeTelemetryapigeetelemetry --> DaemonSetapigeeloggerapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeeloggerapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeemetricsadapterapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeemetricsapigeetelemetryapp
    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeeopentelemetrycollectorapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ServiceAccountapigeeloggerapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ServiceAccountapigeemetricsapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ServiceAccountapigeeopentelemetrycollectorapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> Certificateapigeemetricsadapterapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ApigeeDeploymentapigeemetricsadapterapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ApigeeDeploymentapigeemetricsapigeetelemetryapp
    ApigeeTelemetryapigeetelemetry --> ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> APIServicev1beta1custommetricsk8sio
    DaemonSetapigeeloggerapigeetelemetry --> Podapigeeloggerapigeetelemetry4dhzk
    DaemonSetapigeeloggerapigeetelemetry --> Podapigeeloggerapigeetelemetry69nbt
    DaemonSetapigeeloggerapigeetelemetry --> Podapigeeloggerapigeetelemetry7xjfs
    DaemonSetapigeeloggerapigeetelemetry --> Podapigeeloggerapigeetelemetrylbcpv
    DaemonSetapigeeloggerapigeetelemetry --> Podapigeeloggerapigeetelemetrypfn2z
    DaemonSetapigeeloggerapigeetelemetry --> Podapigeeloggerapigeetelemetryv9srb
    ApigeeDeploymentapigeemetricsadapterapigeetelemetry --> V2HorizontalPodAutoscalerapigeemetricsadapterapigeetelemetry11509fjy0
    ApigeeDeploymentapigeemetricsadapterapigeetelemetry --> ReplicaSetapigeemetricsadapterapigeetelemetry11509fjy0
    ApigeeDeploymentapigeemetricsadapterapigeetelemetry --> Serviceapigeemetricsadapterapigeetelemetry
    ApigeeDeploymentapigeemetricsapigeetelemetryapp --> V2HorizontalPodAutoscalerapigeemetricsapigeetelemetryapp115070qcv
    ApigeeDeploymentapigeemetricsapigeetelemetryapp --> ReplicaSetapigeemetricsapigeetelemetryapp115070qcv
    ApigeeDeploymentapigeemetricsapigeetelemetryapp --> Serviceapigeemetricsapigeetelemetryapp
    ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry --> DaemonSetapigeeopentelemetrycollectorapigeetelemetry
    ReplicaSetapigeemetricsadapterapigeetelemetry11509fjy0 --> Podapigeemetricsadapterapigeetelemetry11509fjy0slzn9
    ReplicaSetapigeemetricsapigeetelemetryapp115070qcv --> Podapigeemetricsapigeetelemetryapp115070qcv2xrjz
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetry45jgc
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetry9jd85
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetrybg6xp
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetryfn8lc
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetryh99tk
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetryk6ls5
    HelmReleasetelemetry --> ApigeeTelemetryapigeetelemetry
```
