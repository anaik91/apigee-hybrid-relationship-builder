Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'telemetry'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 30 related objects.
No filters applied. Including all discovered objects.
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
    ConfigMapapigeemetricsadapterapigeetelemetry["ConfigMap/apigee-metrics-adapter-apigee-telemetry"]
    ConfigMapapigeemetricsapigeetelemetryapp["ConfigMap/apigee-metrics-apigee-telemetry-app"]
    ConfigMapapigeeopentelemetrycollectorapigeetelemetry["ConfigMap/apigee-open-telemetry-collector-apigee-telemetry"]
    ServiceAccountapigeemetricsapigeetelemetry["ServiceAccount/apigee-metrics-apigee-telemetry"]
    ServiceAccountapigeeopentelemetrycollectorapigeetelemetry["ServiceAccount/apigee-open-telemetry-collector-apigee-telemetry"]
    Roleapigeeopentelemetrycollectorapigeetelemetry["Role/apigee-open-telemetry-collector-apigee-telemetry"]
    RoleBindingapigeeopentelemetrycollectorapigeetelemetry["RoleBinding/apigee-open-telemetry-collector-apigee-telemetry"]
    Certificateapigeemetricsadapterapigeetelemetry["Certificate/apigee-metrics-adapter-apigee-telemetry"]
    ApigeeDeploymentapigeemetricsadapterapigeetelemetry["ApigeeDeployment/apigee-metrics-adapter-apigee-telemetry"]
    ApigeeDeploymentapigeemetricsapigeetelemetryapp["ApigeeDeployment/apigee-metrics-apigee-telemetry-app"]
    ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry["ApigeeDeployment/apigee-open-telemetry-collector-apigee-telemetry"]
    V2HorizontalPodAutoscalerapigeemetricsadapterapigeetelemetry1150w5jzc["V2HorizontalPodAutoscaler/apigee-metrics-adapter-apigee-telemetry-1150-w5jzc"]
    ReplicaSetapigeemetricsadapterapigeetelemetry1150w5jzc["ReplicaSet/apigee-metrics-adapter-apigee-telemetry-1150-w5jzc"]
    Serviceapigeemetricsadapterapigeetelemetry["Service/apigee-metrics-adapter-apigee-telemetry"]
    V2HorizontalPodAutoscalerapigeemetricsapigeetelemetryapp11500iu46["V2HorizontalPodAutoscaler/apigee-metrics-apigee-telemetry-app-1150-0iu46"]
    ReplicaSetapigeemetricsapigeetelemetryapp11500iu46["ReplicaSet/apigee-metrics-apigee-telemetry-app-1150-0iu46"]
    Serviceapigeemetricsapigeetelemetryapp["Service/apigee-metrics-apigee-telemetry-app"]
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry["DaemonSet/apigee-open-telemetry-collector-apigee-telemetry"]
    Podapigeemetricsadapterapigeetelemetry1150w5jzcrr845["Pod/apigee-metrics-adapter-apigee-telemetry-1150-w5jzc-rr845"]
    Podapigeemetricsapigeetelemetryapp11500iu46n6hrv["Pod/apigee-metrics-apigee-telemetry-app-1150-0iu46-n6hrv"]
    Podapigeeopentelemetrycollectorapigeetelemetry2fwqn["Pod/apigee-open-telemetry-collector-apigee-telemetry-2fwqn"]
    Podapigeeopentelemetrycollectorapigeetelemetry2snmq["Pod/apigee-open-telemetry-collector-apigee-telemetry-2snmq"]
    Podapigeeopentelemetrycollectorapigeetelemetry4hghh["Pod/apigee-open-telemetry-collector-apigee-telemetry-4hghh"]
    Podapigeeopentelemetrycollectorapigeetelemetry5jp9h["Pod/apigee-open-telemetry-collector-apigee-telemetry-5jp9h"]
    Podapigeeopentelemetrycollectorapigeetelemetryb9mk7["Pod/apigee-open-telemetry-collector-apigee-telemetry-b9mk7"]
    Podapigeeopentelemetrycollectorapigeetelemetryhdgbt["Pod/apigee-open-telemetry-collector-apigee-telemetry-hdgbt"]
    Podapigeeopentelemetrycollectorapigeetelemetryjr56p["Pod/apigee-open-telemetry-collector-apigee-telemetry-jr56p"]
    Podapigeeopentelemetrycollectorapigeetelemetryp7xw8["Pod/apigee-open-telemetry-collector-apigee-telemetry-p7xw8"]
    HelmReleasetelemetry["Helm Release: telemetry"]
    Secretapigeemetricssvcaccount["Secret/apigee-metrics-svc-account"]

    class ApigeeTelemetryapigeetelemetry apigee_crd;
    class ConfigMapapigeemetricsadapterapigeetelemetry config;
    class ConfigMapapigeemetricsapigeetelemetryapp config;
    class ConfigMapapigeeopentelemetrycollectorapigeetelemetry config;
    class ServiceAccountapigeemetricsapigeetelemetry rbac;
    class ServiceAccountapigeeopentelemetrycollectorapigeetelemetry rbac;
    class Roleapigeeopentelemetrycollectorapigeetelemetry rbac;
    class RoleBindingapigeeopentelemetrycollectorapigeetelemetry rbac;
    class Certificateapigeemetricsadapterapigeetelemetry cert_manager_crd;
    class ApigeeDeploymentapigeemetricsadapterapigeetelemetry apigee_crd;
    class ApigeeDeploymentapigeemetricsapigeetelemetryapp apigee_crd;
    class ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry apigee_crd;
    class V2HorizontalPodAutoscalerapigeemetricsadapterapigeetelemetry1150w5jzc workload;
    class ReplicaSetapigeemetricsadapterapigeetelemetry1150w5jzc workload;
    class Serviceapigeemetricsadapterapigeetelemetry network;
    class V2HorizontalPodAutoscalerapigeemetricsapigeetelemetryapp11500iu46 workload;
    class ReplicaSetapigeemetricsapigeetelemetryapp11500iu46 workload;
    class Serviceapigeemetricsapigeetelemetryapp network;
    class DaemonSetapigeeopentelemetrycollectorapigeetelemetry workload;
    class Podapigeemetricsadapterapigeetelemetry1150w5jzcrr845 workload;
    class Podapigeemetricsapigeetelemetryapp11500iu46n6hrv workload;
    class Podapigeeopentelemetrycollectorapigeetelemetry2fwqn workload;
    class Podapigeeopentelemetrycollectorapigeetelemetry2snmq workload;
    class Podapigeeopentelemetrycollectorapigeetelemetry4hghh workload;
    class Podapigeeopentelemetrycollectorapigeetelemetry5jp9h workload;
    class Podapigeeopentelemetrycollectorapigeetelemetryb9mk7 workload;
    class Podapigeeopentelemetrycollectorapigeetelemetryhdgbt workload;
    class Podapigeeopentelemetrycollectorapigeetelemetryjr56p workload;
    class Podapigeeopentelemetrycollectorapigeetelemetryp7xw8 workload;
    class HelmReleasetelemetry helm;
    class Secretapigeemetricssvcaccount config;

    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeemetricsadapterapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeemetricsapigeetelemetryapp
    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeeopentelemetrycollectorapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ServiceAccountapigeemetricsapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ServiceAccountapigeeopentelemetrycollectorapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> Roleapigeeopentelemetrycollectorapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> RoleBindingapigeeopentelemetrycollectorapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> Certificateapigeemetricsadapterapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ApigeeDeploymentapigeemetricsadapterapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ApigeeDeploymentapigeemetricsapigeetelemetryapp
    ApigeeTelemetryapigeetelemetry --> ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry
    ApigeeDeploymentapigeemetricsadapterapigeetelemetry --> V2HorizontalPodAutoscalerapigeemetricsadapterapigeetelemetry1150w5jzc
    ApigeeDeploymentapigeemetricsadapterapigeetelemetry --> ReplicaSetapigeemetricsadapterapigeetelemetry1150w5jzc
    ApigeeDeploymentapigeemetricsadapterapigeetelemetry --> Serviceapigeemetricsadapterapigeetelemetry
    ApigeeDeploymentapigeemetricsapigeetelemetryapp --> V2HorizontalPodAutoscalerapigeemetricsapigeetelemetryapp11500iu46
    ApigeeDeploymentapigeemetricsapigeetelemetryapp --> ReplicaSetapigeemetricsapigeetelemetryapp11500iu46
    ApigeeDeploymentapigeemetricsapigeetelemetryapp --> Serviceapigeemetricsapigeetelemetryapp
    ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry --> DaemonSetapigeeopentelemetrycollectorapigeetelemetry
    ReplicaSetapigeemetricsadapterapigeetelemetry1150w5jzc --> Podapigeemetricsadapterapigeetelemetry1150w5jzcrr845
    ReplicaSetapigeemetricsapigeetelemetryapp11500iu46 --> Podapigeemetricsapigeetelemetryapp11500iu46n6hrv
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetry2fwqn
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetry2snmq
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetry4hghh
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetry5jp9h
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetryb9mk7
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetryhdgbt
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetryjr56p
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetryp7xw8
    HelmReleasetelemetry --> Secretapigeemetricssvcaccount
    HelmReleasetelemetry --> ApigeeTelemetryapigeetelemetry
```
