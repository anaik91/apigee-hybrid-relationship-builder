Deep discovery disabled. Searching for Helm-managed objects only.
Fetching all potential resources for shallow discovery...
Identifying objects directly managed by release 'ingress-manager'...

Discovery complete. Found a total of 9 related objects.
No filters applied. Including all discovered objects.
Building relationship map...
Generating Mermaid diagram with color-coded kinds...

#### Release: ingress-manager | Namespace: apigee
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

    Deploymentapigeeingressgatewaymanager["Deployment/apigee-ingressgateway-manager"]
    ReplicaSetapigeeingressgatewaymanager5967c955ff["ReplicaSet/apigee-ingressgateway-manager-5967c955ff"]
    HelmReleaseingressmanager["Helm Release: ingress-manager"]
    V2HorizontalPodAutoscalerapigeeingressgatewaymanager["V2HorizontalPodAutoscaler/apigee-ingressgateway-manager"]
    Serviceapigeeingressgatewaymanager["Service/apigee-ingressgateway-manager"]
    ConfigMapapigeeenvoyfilters["ConfigMap/apigee-envoyfilters"]
    ConfigMapapigeeistiomeshconfig["ConfigMap/apigee-istio-mesh-config"]
    ServiceAccountapigeeingressgateway["ServiceAccount/apigee-ingressgateway"]
    ServiceAccountapigeeingressgatewaymanager["ServiceAccount/apigee-ingressgateway-manager"]
    Certificateapigeeistiod["Certificate/apigee-istiod"]

    class Deploymentapigeeingressgatewaymanager workload;
    class ReplicaSetapigeeingressgatewaymanager5967c955ff workload;
    class HelmReleaseingressmanager helm;
    class V2HorizontalPodAutoscalerapigeeingressgatewaymanager workload;
    class Serviceapigeeingressgatewaymanager network;
    class ConfigMapapigeeenvoyfilters config;
    class ConfigMapapigeeistiomeshconfig config;
    class ServiceAccountapigeeingressgateway rbac;
    class ServiceAccountapigeeingressgatewaymanager rbac;
    class Certificateapigeeistiod cert_manager_crd;

    Deploymentapigeeingressgatewaymanager --> ReplicaSetapigeeingressgatewaymanager5967c955ff
    HelmReleaseingressmanager --> Deploymentapigeeingressgatewaymanager
    HelmReleaseingressmanager --> V2HorizontalPodAutoscalerapigeeingressgatewaymanager
    HelmReleaseingressmanager --> Serviceapigeeingressgatewaymanager
    HelmReleaseingressmanager --> ConfigMapapigeeenvoyfilters
    HelmReleaseingressmanager --> ConfigMapapigeeistiomeshconfig
    HelmReleaseingressmanager --> ServiceAccountapigeeingressgateway
    HelmReleaseingressmanager --> ServiceAccountapigeeingressgatewaymanager
    HelmReleaseingressmanager --> Certificateapigeeistiod
```
