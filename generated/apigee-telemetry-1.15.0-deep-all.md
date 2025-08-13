Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'telemetry'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 26 related objects.
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
    DaemonSetapigeeloggerapigeetelemetry["DaemonSet/apigee-logger-apigee-telemetry"]
    ConfigMapapigeeloggerapigeetelemetry["ConfigMap/apigee-logger-apigee-telemetry"]
    ConfigMapapigeemetricsadapterapigeetelemetry["ConfigMap/apigee-metrics-adapter-apigee-telemetry"]
    ConfigMapapigeemetricsapigeetelemetryapp["ConfigMap/apigee-metrics-apigee-telemetry-app"]
    ConfigMapapigeeopentelemetrycollectorapigeetelemetry["ConfigMap/apigee-open-telemetry-collector-apigee-telemetry"]
    ServiceAccountapigeeloggerapigeetelemetry["ServiceAccount/apigee-logger-apigee-telemetry"]
    ServiceAccountapigeemetricsapigeetelemetry["ServiceAccount/apigee-metrics-apigee-telemetry"]
    ServiceAccountapigeeopentelemetrycollectorapigeetelemetry["ServiceAccount/apigee-open-telemetry-collector-apigee-telemetry"]
    Roleapigeeopentelemetrycollectorapigeetelemetry["Role/apigee-open-telemetry-collector-apigee-telemetry"]
    RoleBindingapigeeopentelemetrycollectorapigeetelemetry["RoleBinding/apigee-open-telemetry-collector-apigee-telemetry"]
    Certificateapigeemetricsadapterapigeetelemetry["Certificate/apigee-metrics-adapter-apigee-telemetry"]
    ApigeeDeploymentapigeemetricsadapterapigeetelemetry["ApigeeDeployment/apigee-metrics-adapter-apigee-telemetry"]
    ApigeeDeploymentapigeemetricsapigeetelemetryapp["ApigeeDeployment/apigee-metrics-apigee-telemetry-app"]
    ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry["ApigeeDeployment/apigee-open-telemetry-collector-apigee-telemetry"]
    Podapigeeloggerapigeetelemetry476qv["Pod/apigee-logger-apigee-telemetry-476qv"]
    Podapigeeloggerapigeetelemetrysz769["Pod/apigee-logger-apigee-telemetry-sz769"]
    ReplicaSetapigeemetricsadapterapigeetelemetry1150bntz9["ReplicaSet/apigee-metrics-adapter-apigee-telemetry-1150-bntz9"]
    Serviceapigeemetricsadapterapigeetelemetry["Service/apigee-metrics-adapter-apigee-telemetry"]
    ReplicaSetapigeemetricsapigeetelemetryapp11507iavb["ReplicaSet/apigee-metrics-apigee-telemetry-app-1150-7iavb"]
    Serviceapigeemetricsapigeetelemetryapp["Service/apigee-metrics-apigee-telemetry-app"]
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry["DaemonSet/apigee-open-telemetry-collector-apigee-telemetry"]
    Podapigeemetricsadapterapigeetelemetry1150bntz9lvxcd["Pod/apigee-metrics-adapter-apigee-telemetry-1150-bntz9-lvxcd"]
    Podapigeemetricsapigeetelemetryapp11507iavbppqst["Pod/apigee-metrics-apigee-telemetry-app-1150-7iavb-ppqst"]
    Podapigeeopentelemetrycollectorapigeetelemetrydpxs8["Pod/apigee-open-telemetry-collector-apigee-telemetry-dpxs8"]
    Podapigeeopentelemetrycollectorapigeetelemetryvtlhs["Pod/apigee-open-telemetry-collector-apigee-telemetry-vtlhs"]
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
    class Roleapigeeopentelemetrycollectorapigeetelemetry rbac;
    class RoleBindingapigeeopentelemetrycollectorapigeetelemetry rbac;
    class Certificateapigeemetricsadapterapigeetelemetry cert_manager_crd;
    class ApigeeDeploymentapigeemetricsadapterapigeetelemetry apigee_crd;
    class ApigeeDeploymentapigeemetricsapigeetelemetryapp apigee_crd;
    class ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry apigee_crd;
    class Podapigeeloggerapigeetelemetry476qv workload;
    class Podapigeeloggerapigeetelemetrysz769 workload;
    class ReplicaSetapigeemetricsadapterapigeetelemetry1150bntz9 workload;
    class Serviceapigeemetricsadapterapigeetelemetry network;
    class ReplicaSetapigeemetricsapigeetelemetryapp11507iavb workload;
    class Serviceapigeemetricsapigeetelemetryapp network;
    class DaemonSetapigeeopentelemetrycollectorapigeetelemetry workload;
    class Podapigeemetricsadapterapigeetelemetry1150bntz9lvxcd workload;
    class Podapigeemetricsapigeetelemetryapp11507iavbppqst workload;
    class Podapigeeopentelemetrycollectorapigeetelemetrydpxs8 workload;
    class Podapigeeopentelemetrycollectorapigeetelemetryvtlhs workload;
    class HelmReleasetelemetry helm;

    ApigeeTelemetryapigeetelemetry --> DaemonSetapigeeloggerapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeeloggerapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeemetricsadapterapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeemetricsapigeetelemetryapp
    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeeopentelemetrycollectorapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ServiceAccountapigeeloggerapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ServiceAccountapigeemetricsapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ServiceAccountapigeeopentelemetrycollectorapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> Roleapigeeopentelemetrycollectorapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> RoleBindingapigeeopentelemetrycollectorapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> Certificateapigeemetricsadapterapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ApigeeDeploymentapigeemetricsadapterapigeetelemetry
    ApigeeTelemetryapigeetelemetry --> ApigeeDeploymentapigeemetricsapigeetelemetryapp
    ApigeeTelemetryapigeetelemetry --> ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry
    DaemonSetapigeeloggerapigeetelemetry --> Podapigeeloggerapigeetelemetry476qv
    DaemonSetapigeeloggerapigeetelemetry --> Podapigeeloggerapigeetelemetrysz769
    ApigeeDeploymentapigeemetricsadapterapigeetelemetry --> ReplicaSetapigeemetricsadapterapigeetelemetry1150bntz9
    ApigeeDeploymentapigeemetricsadapterapigeetelemetry --> Serviceapigeemetricsadapterapigeetelemetry
    ApigeeDeploymentapigeemetricsapigeetelemetryapp --> ReplicaSetapigeemetricsapigeetelemetryapp11507iavb
    ApigeeDeploymentapigeemetricsapigeetelemetryapp --> Serviceapigeemetricsapigeetelemetryapp
    ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry --> DaemonSetapigeeopentelemetrycollectorapigeetelemetry
    ReplicaSetapigeemetricsadapterapigeetelemetry1150bntz9 --> Podapigeemetricsadapterapigeetelemetry1150bntz9lvxcd
    ReplicaSetapigeemetricsapigeetelemetryapp11507iavb --> Podapigeemetricsapigeetelemetryapp11507iavbppqst
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetrydpxs8
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetryvtlhs
    HelmReleasetelemetry --> ApigeeTelemetryapigeetelemetry
```
