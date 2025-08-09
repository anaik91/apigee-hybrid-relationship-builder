Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'telemetry'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 26 related objects.
Building relationship map...
Generating Mermaid diagram...
#### Release telemetry -> Namespace apigee
```mermaid
graph TD;
    classDef helm fill:#f9f,stroke:#333,stroke-width:2px;
    classDef primitive fill:#d4edda,stroke:#155724,stroke-width:1px;
    classDef apigee_crd fill:#fff3cd,stroke:#856404,stroke-width:2px;
    ApigeeTelemetryapigeetelemetry["ApigeeTelemetry/apigee-telemetry"]
    class ApigeeTelemetryapigeetelemetry apigee_crd;
    DaemonSetapigeeloggerapigeetelemetry["DaemonSet/apigee-logger-apigee-telemetry"]
    class DaemonSetapigeeloggerapigeetelemetry primitive;
    ApigeeTelemetryapigeetelemetry --> DaemonSetapigeeloggerapigeetelemetry
    ConfigMapapigeeloggerapigeetelemetry["ConfigMap/apigee-logger-apigee-telemetry"]
    class ConfigMapapigeeloggerapigeetelemetry primitive;
    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeeloggerapigeetelemetry
    ConfigMapapigeemetricsadapterapigeetelemetry["ConfigMap/apigee-metrics-adapter-apigee-telemetry"]
    class ConfigMapapigeemetricsadapterapigeetelemetry primitive;
    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeemetricsadapterapigeetelemetry
    ConfigMapapigeemetricsapigeetelemetryapp["ConfigMap/apigee-metrics-apigee-telemetry-app"]
    class ConfigMapapigeemetricsapigeetelemetryapp primitive;
    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeemetricsapigeetelemetryapp
    ConfigMapapigeeopentelemetrycollectorapigeetelemetry["ConfigMap/apigee-open-telemetry-collector-apigee-telemetry"]
    class ConfigMapapigeeopentelemetrycollectorapigeetelemetry primitive;
    ApigeeTelemetryapigeetelemetry --> ConfigMapapigeeopentelemetrycollectorapigeetelemetry
    ServiceAccountapigeeloggerapigeetelemetry["ServiceAccount/apigee-logger-apigee-telemetry"]
    class ServiceAccountapigeeloggerapigeetelemetry primitive;
    ApigeeTelemetryapigeetelemetry --> ServiceAccountapigeeloggerapigeetelemetry
    ServiceAccountapigeemetricsapigeetelemetry["ServiceAccount/apigee-metrics-apigee-telemetry"]
    class ServiceAccountapigeemetricsapigeetelemetry primitive;
    ApigeeTelemetryapigeetelemetry --> ServiceAccountapigeemetricsapigeetelemetry
    ServiceAccountapigeeopentelemetrycollectorapigeetelemetry["ServiceAccount/apigee-open-telemetry-collector-apigee-telemetry"]
    class ServiceAccountapigeeopentelemetrycollectorapigeetelemetry primitive;
    ApigeeTelemetryapigeetelemetry --> ServiceAccountapigeeopentelemetrycollectorapigeetelemetry
    Roleapigeeopentelemetrycollectorapigeetelemetry["Role/apigee-open-telemetry-collector-apigee-telemetry"]
    class Roleapigeeopentelemetrycollectorapigeetelemetry primitive;
    ApigeeTelemetryapigeetelemetry --> Roleapigeeopentelemetrycollectorapigeetelemetry
    RoleBindingapigeeopentelemetrycollectorapigeetelemetry["RoleBinding/apigee-open-telemetry-collector-apigee-telemetry"]
    class RoleBindingapigeeopentelemetrycollectorapigeetelemetry primitive;
    ApigeeTelemetryapigeetelemetry --> RoleBindingapigeeopentelemetrycollectorapigeetelemetry
    ApigeeDeploymentapigeemetricsadapterapigeetelemetry["ApigeeDeployment/apigee-metrics-adapter-apigee-telemetry"]
    class ApigeeDeploymentapigeemetricsadapterapigeetelemetry apigee_crd;
    ApigeeTelemetryapigeetelemetry --> ApigeeDeploymentapigeemetricsadapterapigeetelemetry
    ApigeeDeploymentapigeemetricsapigeetelemetryapp["ApigeeDeployment/apigee-metrics-apigee-telemetry-app"]
    class ApigeeDeploymentapigeemetricsapigeetelemetryapp apigee_crd;
    ApigeeTelemetryapigeetelemetry --> ApigeeDeploymentapigeemetricsapigeetelemetryapp
    ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry["ApigeeDeployment/apigee-open-telemetry-collector-apigee-telemetry"]
    class ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry apigee_crd;
    ApigeeTelemetryapigeetelemetry --> ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry
    Certificateapigeemetricsadapterapigeetelemetry["Certificate/apigee-metrics-adapter-apigee-telemetry"]
    class Certificateapigeemetricsadapterapigeetelemetry primitive;
    ApigeeTelemetryapigeetelemetry --> Certificateapigeemetricsadapterapigeetelemetry
    Podapigeeloggerapigeetelemetry476qv["Pod/apigee-logger-apigee-telemetry-476qv"]
    class Podapigeeloggerapigeetelemetry476qv primitive;
    DaemonSetapigeeloggerapigeetelemetry --> Podapigeeloggerapigeetelemetry476qv
    Podapigeeloggerapigeetelemetrysz769["Pod/apigee-logger-apigee-telemetry-sz769"]
    class Podapigeeloggerapigeetelemetrysz769 primitive;
    DaemonSetapigeeloggerapigeetelemetry --> Podapigeeloggerapigeetelemetrysz769
    ReplicaSetapigeemetricsadapterapigeetelemetry1150bntz9["ReplicaSet/apigee-metrics-adapter-apigee-telemetry-1150-bntz9"]
    class ReplicaSetapigeemetricsadapterapigeetelemetry1150bntz9 primitive;
    ApigeeDeploymentapigeemetricsadapterapigeetelemetry --> ReplicaSetapigeemetricsadapterapigeetelemetry1150bntz9
    Serviceapigeemetricsadapterapigeetelemetry["Service/apigee-metrics-adapter-apigee-telemetry"]
    class Serviceapigeemetricsadapterapigeetelemetry primitive;
    ApigeeDeploymentapigeemetricsadapterapigeetelemetry --> Serviceapigeemetricsadapterapigeetelemetry
    ReplicaSetapigeemetricsapigeetelemetryapp11507iavb["ReplicaSet/apigee-metrics-apigee-telemetry-app-1150-7iavb"]
    class ReplicaSetapigeemetricsapigeetelemetryapp11507iavb primitive;
    ApigeeDeploymentapigeemetricsapigeetelemetryapp --> ReplicaSetapigeemetricsapigeetelemetryapp11507iavb
    Serviceapigeemetricsapigeetelemetryapp["Service/apigee-metrics-apigee-telemetry-app"]
    class Serviceapigeemetricsapigeetelemetryapp primitive;
    ApigeeDeploymentapigeemetricsapigeetelemetryapp --> Serviceapigeemetricsapigeetelemetryapp
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry["DaemonSet/apigee-open-telemetry-collector-apigee-telemetry"]
    class DaemonSetapigeeopentelemetrycollectorapigeetelemetry primitive;
    ApigeeDeploymentapigeeopentelemetrycollectorapigeetelemetry --> DaemonSetapigeeopentelemetrycollectorapigeetelemetry
    Podapigeemetricsadapterapigeetelemetry1150bntz9lvxcd["Pod/apigee-metrics-adapter-apigee-telemetry-1150-bntz9-lvxcd"]
    class Podapigeemetricsadapterapigeetelemetry1150bntz9lvxcd primitive;
    ReplicaSetapigeemetricsadapterapigeetelemetry1150bntz9 --> Podapigeemetricsadapterapigeetelemetry1150bntz9lvxcd
    Podapigeemetricsapigeetelemetryapp11507iavbppqst["Pod/apigee-metrics-apigee-telemetry-app-1150-7iavb-ppqst"]
    class Podapigeemetricsapigeetelemetryapp11507iavbppqst primitive;
    ReplicaSetapigeemetricsapigeetelemetryapp11507iavb --> Podapigeemetricsapigeetelemetryapp11507iavbppqst
    Podapigeeopentelemetrycollectorapigeetelemetrydpxs8["Pod/apigee-open-telemetry-collector-apigee-telemetry-dpxs8"]
    class Podapigeeopentelemetrycollectorapigeetelemetrydpxs8 primitive;
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetrydpxs8
    Podapigeeopentelemetrycollectorapigeetelemetryvtlhs["Pod/apigee-open-telemetry-collector-apigee-telemetry-vtlhs"]
    class Podapigeeopentelemetrycollectorapigeetelemetryvtlhs primitive;
    DaemonSetapigeeopentelemetrycollectorapigeetelemetry --> Podapigeeopentelemetrycollectorapigeetelemetryvtlhs
    HelmReleasetelemetry["Helm Release: telemetry"]
    class HelmReleasetelemetry helm;
    HelmReleasetelemetry --> ApigeeTelemetryapigeetelemetry
```
