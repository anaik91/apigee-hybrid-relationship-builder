Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'ingress-manager'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 11 related objects.
Building relationship map...
Generating Mermaid diagram...
#### Release ingress-manager -> Namespace apigee
```mermaid
graph TD;
    classDef helm fill:#f9f,stroke:#333,stroke-width:2px;
    classDef primitive fill:#d4edda,stroke:#155724,stroke-width:1px;
    classDef apigee_crd fill:#fff3cd,stroke:#856404,stroke-width:2px;
    Deploymentapigeeingressgatewaymanager["Deployment/apigee-ingressgateway-manager"]
    class Deploymentapigeeingressgatewaymanager primitive;
    ReplicaSetapigeeingressgatewaymanager54b5799f4d["ReplicaSet/apigee-ingressgateway-manager-54b5799f4d"]
    class ReplicaSetapigeeingressgatewaymanager54b5799f4d primitive;
    Deploymentapigeeingressgatewaymanager --> ReplicaSetapigeeingressgatewaymanager54b5799f4d
    ReplicaSetapigeeingressgatewaymanager5967c955ff["ReplicaSet/apigee-ingressgateway-manager-5967c955ff"]
    class ReplicaSetapigeeingressgatewaymanager5967c955ff primitive;
    Deploymentapigeeingressgatewaymanager --> ReplicaSetapigeeingressgatewaymanager5967c955ff
    Podapigeeingressgatewaymanager54b5799f4d7gchs["Pod/apigee-ingressgateway-manager-54b5799f4d-7gchs"]
    class Podapigeeingressgatewaymanager54b5799f4d7gchs primitive;
    ReplicaSetapigeeingressgatewaymanager54b5799f4d --> Podapigeeingressgatewaymanager54b5799f4d7gchs
    Podapigeeingressgatewaymanager54b5799f4dhbwth["Pod/apigee-ingressgateway-manager-54b5799f4d-hbwth"]
    class Podapigeeingressgatewaymanager54b5799f4dhbwth primitive;
    ReplicaSetapigeeingressgatewaymanager54b5799f4d --> Podapigeeingressgatewaymanager54b5799f4dhbwth
    HelmReleaseingressmanager["Helm Release: ingress-manager"]
    class HelmReleaseingressmanager helm;
    HelmReleaseingressmanager --> Deploymentapigeeingressgatewaymanager
    Serviceapigeeingressgatewaymanager["Service/apigee-ingressgateway-manager"]
    class Serviceapigeeingressgatewaymanager primitive;
    HelmReleaseingressmanager --> Serviceapigeeingressgatewaymanager
    ConfigMapapigeeenvoyfilters["ConfigMap/apigee-envoyfilters"]
    class ConfigMapapigeeenvoyfilters primitive;
    HelmReleaseingressmanager --> ConfigMapapigeeenvoyfilters
    ConfigMapapigeeistiomeshconfig["ConfigMap/apigee-istio-mesh-config"]
    class ConfigMapapigeeistiomeshconfig primitive;
    HelmReleaseingressmanager --> ConfigMapapigeeistiomeshconfig
    ServiceAccountapigeeingressgateway["ServiceAccount/apigee-ingressgateway"]
    class ServiceAccountapigeeingressgateway primitive;
    HelmReleaseingressmanager --> ServiceAccountapigeeingressgateway
    ServiceAccountapigeeingressgatewaymanager["ServiceAccount/apigee-ingressgateway-manager"]
    class ServiceAccountapigeeingressgatewaymanager primitive;
    HelmReleaseingressmanager --> ServiceAccountapigeeingressgatewaymanager
    Certificateapigeeistiod["Certificate/apigee-istiod"]
    class Certificateapigeeistiod primitive;
    HelmReleaseingressmanager --> Certificateapigeeistiod
```
