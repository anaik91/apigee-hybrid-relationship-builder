Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'redis'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 17 related objects.
Building relationship map...
Generating Mermaid diagram...
#### Release redis -> Namespace apigee
```mermaid
graph TD;
    classDef helm fill:#f9f,stroke:#333,stroke-width:2px;
    classDef primitive fill:#d4edda,stroke:#155724,stroke-width:1px;
    classDef apigee_crd fill:#fff3cd,stroke:#856404,stroke-width:2px;
    ApigeeRedisdefault["ApigeeRedis/default"]
    class ApigeeRedisdefault apigee_crd;
    StatefulSetapigeeredisdefault["StatefulSet/apigee-redis-default"]
    class StatefulSetapigeeredisdefault primitive;
    ApigeeRedisdefault --> StatefulSetapigeeredisdefault
    Serviceapigeeredisdefault["Service/apigee-redis-default"]
    class Serviceapigeeredisdefault primitive;
    ApigeeRedisdefault --> Serviceapigeeredisdefault
    ConfigMapapigeeredisenvoystaticconfig["ConfigMap/apigee-redis-envoy-static-config"]
    class ConfigMapapigeeredisenvoystaticconfig primitive;
    ApigeeRedisdefault --> ConfigMapapigeeredisenvoystaticconfig
    Secretapigeeredisconfig["Secret/apigee-redis-config"]
    class Secretapigeeredisconfig primitive;
    ApigeeRedisdefault --> Secretapigeeredisconfig
    Secretapigeeredisdefaultcredsce6e0e["Secret/apigee-redis-default-creds-ce6e0e"]
    class Secretapigeeredisdefaultcredsce6e0e primitive;
    ApigeeRedisdefault --> Secretapigeeredisdefaultcredsce6e0e
    ServiceAccountapigeeredisdefault["ServiceAccount/apigee-redis-default"]
    class ServiceAccountapigeeredisdefault primitive;
    ApigeeRedisdefault --> ServiceAccountapigeeredisdefault
    ServiceAccountapigeeredisenvoydefault["ServiceAccount/apigee-redis-envoy-default"]
    class ServiceAccountapigeeredisenvoydefault primitive;
    ApigeeRedisdefault --> ServiceAccountapigeeredisenvoydefault
    ApigeeDeploymentapigeeredisenvoydefault["ApigeeDeployment/apigee-redis-envoy-default"]
    class ApigeeDeploymentapigeeredisenvoydefault apigee_crd;
    ApigeeRedisdefault --> ApigeeDeploymentapigeeredisenvoydefault
    Certificateapigeeredisdefault["Certificate/apigee-redis-default"]
    class Certificateapigeeredisdefault primitive;
    ApigeeRedisdefault --> Certificateapigeeredisdefault
    Certificateapigeeredisenvoydefault["Certificate/apigee-redis-envoy-default"]
    class Certificateapigeeredisenvoydefault primitive;
    ApigeeRedisdefault --> Certificateapigeeredisenvoydefault
    Podapigeeredisdefault0["Pod/apigee-redis-default-0"]
    class Podapigeeredisdefault0 primitive;
    StatefulSetapigeeredisdefault --> Podapigeeredisdefault0
    Podapigeeredisdefault1["Pod/apigee-redis-default-1"]
    class Podapigeeredisdefault1 primitive;
    StatefulSetapigeeredisdefault --> Podapigeeredisdefault1
    ReplicaSetapigeeredisenvoydefault1150vvwgv["ReplicaSet/apigee-redis-envoy-default-1150-vvwgv"]
    class ReplicaSetapigeeredisenvoydefault1150vvwgv primitive;
    ApigeeDeploymentapigeeredisenvoydefault --> ReplicaSetapigeeredisenvoydefault1150vvwgv
    Serviceapigeeredisenvoydefault["Service/apigee-redis-envoy-default"]
    class Serviceapigeeredisenvoydefault primitive;
    ApigeeDeploymentapigeeredisenvoydefault --> Serviceapigeeredisenvoydefault
    Podapigeeredisenvoydefault1150vvwgv4gbtx["Pod/apigee-redis-envoy-default-1150-vvwgv-4gbtx"]
    class Podapigeeredisenvoydefault1150vvwgv4gbtx primitive;
    ReplicaSetapigeeredisenvoydefault1150vvwgv --> Podapigeeredisenvoydefault1150vvwgv4gbtx
    HelmReleaseredis["Helm Release: redis"]
    class HelmReleaseredis helm;
    Secretapigeeredisdefaultcreds["Secret/apigee-redis-default-creds"]
    class Secretapigeeredisdefaultcreds primitive;
    HelmReleaseredis --> Secretapigeeredisdefaultcreds
    HelmReleaseredis --> ApigeeRedisdefault
```
