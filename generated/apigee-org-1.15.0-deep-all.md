Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'apigee-hw'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 59 related objects.
No filters applied. Including all discovered objects.
Building relationship map...
Generating Mermaid diagram with color-coded kinds...

#### Release: apigee-hw | Namespace: apigee
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

    ApigeeOrganizationapigeehw02a578b["ApigeeOrganization/apigee-hw-02a578b"]
    ConfigMapapigeecassandraschemavalapigeehw02a578b["ConfigMap/apigee-cassandra-schema-val-apigee-hw-02a578b"]
    ConfigMapapigeeudcaapigeehw02a578bfluentdconfig["ConfigMap/apigee-udca-apigee-hw-02a578b-fluentd-config"]
    Secretapigeemartapigeehw02a578bconfig6abffb["Secret/apigee-mart-apigee-hw-02a578b-config-6abffb"]
    ServiceAccountapigeecassandraschemasetupapigeehw02a578b["ServiceAccount/apigee-cassandra-schema-setup-apigee-hw-02a578b"]
    ServiceAccountapigeecassandraschemavalapigeehw02a578b["ServiceAccount/apigee-cassandra-schema-val-apigee-hw-02a578b"]
    ServiceAccountapigeecassandrausersetupapigeehw02a578b["ServiceAccount/apigee-cassandra-user-setup-apigee-hw-02a578b"]
    ServiceAccountapigeeconnectagentapigeehw02a578b["ServiceAccount/apigee-connect-agent-apigee-hw-02a578b"]
    ServiceAccountapigeeingressgatewayapigeehw02a578b["ServiceAccount/apigee-ingressgateway-apigee-hw-02a578b"]
    ServiceAccountapigeemartapigeehw02a578b["ServiceAccount/apigee-mart-apigee-hw-02a578b"]
    ServiceAccountapigeeruntimeapigeehwdeve8f1e25["ServiceAccount/apigee-runtime-apigee-hw-dev-e8f1e25"]
    ServiceAccountapigeeudcaapigeehw02a578b["ServiceAccount/apigee-udca-apigee-hw-02a578b"]
    ServiceAccountapigeewatcherapigeehw02a578b["ServiceAccount/apigee-watcher-apigee-hw-02a578b"]
    Roleapigeecassandraschemavalapigeehw02a578b["Role/apigee-cassandra-schema-val-apigee-hw-02a578b"]
    Roleapigeeingressgatewayapigeehw02a578b["Role/apigee-ingressgateway-apigee-hw-02a578b"]
    Roleapigeewatcherapigeehw02a578b["Role/apigee-watcher-apigee-hw-02a578b"]
    RoleBindingapigeecassandraschemavalapigeehw02a578b["RoleBinding/apigee-cassandra-schema-val-apigee-hw-02a578b"]
    RoleBindingapigeeingressgatewayapigeehw02a578b["RoleBinding/apigee-ingressgateway-apigee-hw-02a578b"]
    RoleBindingapigeewatcherapigeehw02a578b["RoleBinding/apigee-watcher-apigee-hw-02a578b"]
    Certificateapigeecassandraschemasetupapigeehw02a578b["Certificate/apigee-cassandra-schema-setup-apigee-hw-02a578b"]
    Certificateapigeecassandraschemavalapigeehw02a578b["Certificate/apigee-cassandra-schema-val-apigee-hw-02a578b"]
    Certificateapigeecassandrausersetupapigeehw02a578b["Certificate/apigee-cassandra-user-setup-apigee-hw-02a578b"]
    Certificateapigeeconnectagentapigeehw02a578b["Certificate/apigee-connect-agent-apigee-hw-02a578b"]
    Certificateapigeemartapigeehw02a578b["Certificate/apigee-mart-apigee-hw-02a578b"]
    Certificateapigeeudcaapigeehw02a578b["Certificate/apigee-udca-apigee-hw-02a578b"]
    Certificateapigeewatcherapigeehw02a578b["Certificate/apigee-watcher-apigee-hw-02a578b"]
    ApigeeDeploymentapigeeconnectagentapigeehw02a578b["ApigeeDeployment/apigee-connect-agent-apigee-hw-02a578b"]
    ApigeeDeploymentapigeeingressgatewaygroupaapigeehw02a578b["ApigeeDeployment/apigee-ingressgateway-group-a-apigee-hw-02a578b"]
    ApigeeDeploymentapigeemartapigeehw02a578b["ApigeeDeployment/apigee-mart-apigee-hw-02a578b"]
    ApigeeDeploymentapigeeudcaapigeehw02a578b["ApigeeDeployment/apigee-udca-apigee-hw-02a578b"]
    ApigeeDeploymentapigeewatcherapigeehw02a578b["ApigeeDeployment/apigee-watcher-apigee-hw-02a578b"]
    V2HorizontalPodAutoscalerapigeeconnectagentapigeehw02a578b1150wg9ln["V2HorizontalPodAutoscaler/apigee-connect-agent-apigee-hw-02a578b-1150-wg9ln"]
    ReplicaSetapigeeconnectagentapigeehw02a578b1150wg9ln["ReplicaSet/apigee-connect-agent-apigee-hw-02a578b-1150-wg9ln"]
    Serviceapigeeconnectagentapigeehw02a578b["Service/apigee-connect-agent-apigee-hw-02a578b"]
    V2HorizontalPodAutoscalerapigeeingressgatewaygroupaapigeehw02a578b115075abx["V2HorizontalPodAutoscaler/apigee-ingressgateway-group-a-apigee-hw-02a578b-1150-75abx"]
    ReplicaSetapigeeingressgatewaygroupaapigeehw02a578b115075abx["ReplicaSet/apigee-ingressgateway-group-a-apigee-hw-02a578b-1150-75abx"]
    Serviceapigeeingressgatewaygroupaapigeehw02a578b["Service/apigee-ingressgateway-group-a-apigee-hw-02a578b"]
    V2HorizontalPodAutoscalerapigeemartapigeehw02a578b1150vnp7p["V2HorizontalPodAutoscaler/apigee-mart-apigee-hw-02a578b-1150-vnp7p"]
    ReplicaSetapigeemartapigeehw02a578b1150vnp7p["ReplicaSet/apigee-mart-apigee-hw-02a578b-1150-vnp7p"]
    Serviceapigeemartapigeehw02a578b["Service/apigee-mart-apigee-hw-02a578b"]
    V2HorizontalPodAutoscalerapigeeudcaapigeehw02a578b1150l6k9l["V2HorizontalPodAutoscaler/apigee-udca-apigee-hw-02a578b-1150-l6k9l"]
    ReplicaSetapigeeudcaapigeehw02a578b1150l6k9l["ReplicaSet/apigee-udca-apigee-hw-02a578b-1150-l6k9l"]
    Serviceapigeeudcaapigeehw02a578b["Service/apigee-udca-apigee-hw-02a578b"]
    V2HorizontalPodAutoscalerapigeewatcherapigeehw02a578b1150qehyr["V2HorizontalPodAutoscaler/apigee-watcher-apigee-hw-02a578b-1150-qehyr"]
    ReplicaSetapigeewatcherapigeehw02a578b1150qehyr["ReplicaSet/apigee-watcher-apigee-hw-02a578b-1150-qehyr"]
    Serviceapigeewatcherapigeehw02a578b["Service/apigee-watcher-apigee-hw-02a578b"]
    Podapigeeconnectagentapigeehw02a578b1150wg9ln2pq57["Pod/apigee-connect-agent-apigee-hw-02a578b-1150-wg9ln-2pq57"]
    Podapigeeingressgatewaygroupaapigeehw02a578b115075abxhqllg["Pod/apigee-ingressgateway-group-a-apigee-hw-02a578b-1150-75abxhqllg"]
    Podapigeeingressgatewaygroupaapigeehw02a578b115075abxxdsdl["Pod/apigee-ingressgateway-group-a-apigee-hw-02a578b-1150-75abxxdsdl"]
    Podapigeemartapigeehw02a578b1150vnp7pjzgrq["Pod/apigee-mart-apigee-hw-02a578b-1150-vnp7p-jzgrq"]
    Podapigeeudcaapigeehw02a578b1150l6k9lfh92m["Pod/apigee-udca-apigee-hw-02a578b-1150-l6k9l-fh92m"]
    Podapigeewatcherapigeehw02a578b1150qehyrchvgh["Pod/apigee-watcher-apigee-hw-02a578b-1150-qehyr-chvgh"]
    HelmReleaseapigeehw["Helm Release: apigee-hw"]
    Secretapigeeconnectagentapigeehw02a578bsvcaccount["Secret/apigee-connect-agent-apigee-hw-02a578b-svc-account"]
    Secretapigeehw02a578baxsalt["Secret/apigee-hw-02a578b-ax-salt"]
    Secretapigeehw02a578bdataencryption["Secret/apigee-hw-02a578b-data-encryption"]
    Secretapigeehw02a578bencryptionkeys["Secret/apigee-hw-02a578b-encryption-keys"]
    Secretapigeemartapigeehw02a578bsvcaccount["Secret/apigee-mart-apigee-hw-02a578b-svc-account"]
    Secretapigeeudcaapigeehw02a578bsvcaccount["Secret/apigee-udca-apigee-hw-02a578b-svc-account"]
    Secretapigeewatcherapigeehw02a578bsvcaccount["Secret/apigee-watcher-apigee-hw-02a578b-svc-account"]

    class ApigeeOrganizationapigeehw02a578b apigee_crd;
    class ConfigMapapigeecassandraschemavalapigeehw02a578b config;
    class ConfigMapapigeeudcaapigeehw02a578bfluentdconfig config;
    class Secretapigeemartapigeehw02a578bconfig6abffb config;
    class ServiceAccountapigeecassandraschemasetupapigeehw02a578b rbac;
    class ServiceAccountapigeecassandraschemavalapigeehw02a578b rbac;
    class ServiceAccountapigeecassandrausersetupapigeehw02a578b rbac;
    class ServiceAccountapigeeconnectagentapigeehw02a578b rbac;
    class ServiceAccountapigeeingressgatewayapigeehw02a578b rbac;
    class ServiceAccountapigeemartapigeehw02a578b rbac;
    class ServiceAccountapigeeruntimeapigeehwdeve8f1e25 rbac;
    class ServiceAccountapigeeudcaapigeehw02a578b rbac;
    class ServiceAccountapigeewatcherapigeehw02a578b rbac;
    class Roleapigeecassandraschemavalapigeehw02a578b rbac;
    class Roleapigeeingressgatewayapigeehw02a578b rbac;
    class Roleapigeewatcherapigeehw02a578b rbac;
    class RoleBindingapigeecassandraschemavalapigeehw02a578b rbac;
    class RoleBindingapigeeingressgatewayapigeehw02a578b rbac;
    class RoleBindingapigeewatcherapigeehw02a578b rbac;
    class Certificateapigeecassandraschemasetupapigeehw02a578b cert_manager_crd;
    class Certificateapigeecassandraschemavalapigeehw02a578b cert_manager_crd;
    class Certificateapigeecassandrausersetupapigeehw02a578b cert_manager_crd;
    class Certificateapigeeconnectagentapigeehw02a578b cert_manager_crd;
    class Certificateapigeemartapigeehw02a578b cert_manager_crd;
    class Certificateapigeeudcaapigeehw02a578b cert_manager_crd;
    class Certificateapigeewatcherapigeehw02a578b cert_manager_crd;
    class ApigeeDeploymentapigeeconnectagentapigeehw02a578b apigee_crd;
    class ApigeeDeploymentapigeeingressgatewaygroupaapigeehw02a578b apigee_crd;
    class ApigeeDeploymentapigeemartapigeehw02a578b apigee_crd;
    class ApigeeDeploymentapigeeudcaapigeehw02a578b apigee_crd;
    class ApigeeDeploymentapigeewatcherapigeehw02a578b apigee_crd;
    class V2HorizontalPodAutoscalerapigeeconnectagentapigeehw02a578b1150wg9ln workload;
    class ReplicaSetapigeeconnectagentapigeehw02a578b1150wg9ln workload;
    class Serviceapigeeconnectagentapigeehw02a578b network;
    class V2HorizontalPodAutoscalerapigeeingressgatewaygroupaapigeehw02a578b115075abx workload;
    class ReplicaSetapigeeingressgatewaygroupaapigeehw02a578b115075abx workload;
    class Serviceapigeeingressgatewaygroupaapigeehw02a578b network;
    class V2HorizontalPodAutoscalerapigeemartapigeehw02a578b1150vnp7p workload;
    class ReplicaSetapigeemartapigeehw02a578b1150vnp7p workload;
    class Serviceapigeemartapigeehw02a578b network;
    class V2HorizontalPodAutoscalerapigeeudcaapigeehw02a578b1150l6k9l workload;
    class ReplicaSetapigeeudcaapigeehw02a578b1150l6k9l workload;
    class Serviceapigeeudcaapigeehw02a578b network;
    class V2HorizontalPodAutoscalerapigeewatcherapigeehw02a578b1150qehyr workload;
    class ReplicaSetapigeewatcherapigeehw02a578b1150qehyr workload;
    class Serviceapigeewatcherapigeehw02a578b network;
    class Podapigeeconnectagentapigeehw02a578b1150wg9ln2pq57 workload;
    class Podapigeeingressgatewaygroupaapigeehw02a578b115075abxhqllg workload;
    class Podapigeeingressgatewaygroupaapigeehw02a578b115075abxxdsdl workload;
    class Podapigeemartapigeehw02a578b1150vnp7pjzgrq workload;
    class Podapigeeudcaapigeehw02a578b1150l6k9lfh92m workload;
    class Podapigeewatcherapigeehw02a578b1150qehyrchvgh workload;
    class HelmReleaseapigeehw helm;
    class Secretapigeeconnectagentapigeehw02a578bsvcaccount config;
    class Secretapigeehw02a578baxsalt config;
    class Secretapigeehw02a578bdataencryption config;
    class Secretapigeehw02a578bencryptionkeys config;
    class Secretapigeemartapigeehw02a578bsvcaccount config;
    class Secretapigeeudcaapigeehw02a578bsvcaccount config;
    class Secretapigeewatcherapigeehw02a578bsvcaccount config;

    ApigeeOrganizationapigeehw02a578b --> ConfigMapapigeecassandraschemavalapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> ConfigMapapigeeudcaapigeehw02a578bfluentdconfig
    ApigeeOrganizationapigeehw02a578b --> Secretapigeemartapigeehw02a578bconfig6abffb
    ApigeeOrganizationapigeehw02a578b --> ServiceAccountapigeecassandraschemasetupapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> ServiceAccountapigeecassandraschemavalapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> ServiceAccountapigeecassandrausersetupapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> ServiceAccountapigeeconnectagentapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> ServiceAccountapigeeingressgatewayapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> ServiceAccountapigeemartapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> ServiceAccountapigeeruntimeapigeehwdeve8f1e25
    ApigeeOrganizationapigeehw02a578b --> ServiceAccountapigeeudcaapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> ServiceAccountapigeewatcherapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> Roleapigeecassandraschemavalapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> Roleapigeeingressgatewayapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> Roleapigeewatcherapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> RoleBindingapigeecassandraschemavalapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> RoleBindingapigeeingressgatewayapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> RoleBindingapigeewatcherapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> Certificateapigeecassandraschemasetupapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> Certificateapigeecassandraschemavalapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> Certificateapigeecassandrausersetupapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> Certificateapigeeconnectagentapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> Certificateapigeemartapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> Certificateapigeeudcaapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> Certificateapigeewatcherapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> ApigeeDeploymentapigeeconnectagentapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> ApigeeDeploymentapigeeingressgatewaygroupaapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> ApigeeDeploymentapigeemartapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> ApigeeDeploymentapigeeudcaapigeehw02a578b
    ApigeeOrganizationapigeehw02a578b --> ApigeeDeploymentapigeewatcherapigeehw02a578b
    ApigeeDeploymentapigeeconnectagentapigeehw02a578b --> V2HorizontalPodAutoscalerapigeeconnectagentapigeehw02a578b1150wg9ln
    ApigeeDeploymentapigeeconnectagentapigeehw02a578b --> ReplicaSetapigeeconnectagentapigeehw02a578b1150wg9ln
    ApigeeDeploymentapigeeconnectagentapigeehw02a578b --> Serviceapigeeconnectagentapigeehw02a578b
    ApigeeDeploymentapigeeingressgatewaygroupaapigeehw02a578b --> V2HorizontalPodAutoscalerapigeeingressgatewaygroupaapigeehw02a578b115075abx
    ApigeeDeploymentapigeeingressgatewaygroupaapigeehw02a578b --> ReplicaSetapigeeingressgatewaygroupaapigeehw02a578b115075abx
    ApigeeDeploymentapigeeingressgatewaygroupaapigeehw02a578b --> Serviceapigeeingressgatewaygroupaapigeehw02a578b
    ApigeeDeploymentapigeemartapigeehw02a578b --> V2HorizontalPodAutoscalerapigeemartapigeehw02a578b1150vnp7p
    ApigeeDeploymentapigeemartapigeehw02a578b --> ReplicaSetapigeemartapigeehw02a578b1150vnp7p
    ApigeeDeploymentapigeemartapigeehw02a578b --> Serviceapigeemartapigeehw02a578b
    ApigeeDeploymentapigeeudcaapigeehw02a578b --> V2HorizontalPodAutoscalerapigeeudcaapigeehw02a578b1150l6k9l
    ApigeeDeploymentapigeeudcaapigeehw02a578b --> ReplicaSetapigeeudcaapigeehw02a578b1150l6k9l
    ApigeeDeploymentapigeeudcaapigeehw02a578b --> Serviceapigeeudcaapigeehw02a578b
    ApigeeDeploymentapigeewatcherapigeehw02a578b --> V2HorizontalPodAutoscalerapigeewatcherapigeehw02a578b1150qehyr
    ApigeeDeploymentapigeewatcherapigeehw02a578b --> ReplicaSetapigeewatcherapigeehw02a578b1150qehyr
    ApigeeDeploymentapigeewatcherapigeehw02a578b --> Serviceapigeewatcherapigeehw02a578b
    ReplicaSetapigeeconnectagentapigeehw02a578b1150wg9ln --> Podapigeeconnectagentapigeehw02a578b1150wg9ln2pq57
    ReplicaSetapigeeingressgatewaygroupaapigeehw02a578b115075abx --> Podapigeeingressgatewaygroupaapigeehw02a578b115075abxhqllg
    ReplicaSetapigeeingressgatewaygroupaapigeehw02a578b115075abx --> Podapigeeingressgatewaygroupaapigeehw02a578b115075abxxdsdl
    ReplicaSetapigeemartapigeehw02a578b1150vnp7p --> Podapigeemartapigeehw02a578b1150vnp7pjzgrq
    ReplicaSetapigeeudcaapigeehw02a578b1150l6k9l --> Podapigeeudcaapigeehw02a578b1150l6k9lfh92m
    ReplicaSetapigeewatcherapigeehw02a578b1150qehyr --> Podapigeewatcherapigeehw02a578b1150qehyrchvgh
    HelmReleaseapigeehw --> Secretapigeeconnectagentapigeehw02a578bsvcaccount
    HelmReleaseapigeehw --> Secretapigeehw02a578baxsalt
    HelmReleaseapigeehw --> Secretapigeehw02a578bdataencryption
    HelmReleaseapigeehw --> Secretapigeehw02a578bencryptionkeys
    HelmReleaseapigeehw --> Secretapigeemartapigeehw02a578bsvcaccount
    HelmReleaseapigeehw --> Secretapigeeudcaapigeehw02a578bsvcaccount
    HelmReleaseapigeehw --> Secretapigeewatcherapigeehw02a578bsvcaccount
    HelmReleaseapigeehw --> ApigeeOrganizationapigeehw02a578b
```
