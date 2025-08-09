Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'ci-cloud-spanner-c06d'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 57 related objects.
Building relationship map...
Generating Mermaid diagram...
#### Release ci-cloud-spanner-c06d -> Namespace apigee
```mermaid
graph TD;
    classDef helm fill:#f9f,stroke:#333,stroke-width:2px;
    classDef primitive fill:#d4edda,stroke:#155724,stroke-width:1px;
    classDef apigee_crd fill:#fff3cd,stroke:#856404,stroke-width:2px;
    ApigeeOrganizationcicloudspanne660f3fb["ApigeeOrganization/ci-cloud-spanne-660f3fb"]
    class ApigeeOrganizationcicloudspanne660f3fb apigee_crd;
    ConfigMapapigeecassandraschemavalcicloudspanne660f3fb["ConfigMap/apigee-cassandra-schema-val-ci-cloud-spanne-660f3fb"]
    class ConfigMapapigeecassandraschemavalcicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> ConfigMapapigeecassandraschemavalcicloudspanne660f3fb
    ConfigMapapigeeudcacicloudspanne660f3fbfluentdconfig["ConfigMap/apigee-udca-ci-cloud-spanne-660f3fb-fluentd-config"]
    class ConfigMapapigeeudcacicloudspanne660f3fbfluentdconfig primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> ConfigMapapigeeudcacicloudspanne660f3fbfluentdconfig
    Secretapigeemartcicloudspanne660f3fbconfig1a6a79["Secret/apigee-mart-ci-cloud-spanne-660f3fb-config-1a6a79"]
    class Secretapigeemartcicloudspanne660f3fbconfig1a6a79 primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> Secretapigeemartcicloudspanne660f3fbconfig1a6a79
    ServiceAccountapigeecassandraschemasetupcicloudspanne660f3fb["ServiceAccount/apigee-cassandra-schema-setup-ci-cloud-spanne-660f3fb"]
    class ServiceAccountapigeecassandraschemasetupcicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeecassandraschemasetupcicloudspanne660f3fb
    ServiceAccountapigeecassandraschemavalcicloudspanne660f3fb["ServiceAccount/apigee-cassandra-schema-val-ci-cloud-spanne-660f3fb"]
    class ServiceAccountapigeecassandraschemavalcicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeecassandraschemavalcicloudspanne660f3fb
    ServiceAccountapigeecassandrausersetupcicloudspanne660f3fb["ServiceAccount/apigee-cassandra-user-setup-ci-cloud-spanne-660f3fb"]
    class ServiceAccountapigeecassandrausersetupcicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeecassandrausersetupcicloudspanne660f3fb
    ServiceAccountapigeeconnectagentcicloudspanne660f3fb["ServiceAccount/apigee-connect-agent-ci-cloud-spanne-660f3fb"]
    class ServiceAccountapigeeconnectagentcicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeeconnectagentcicloudspanne660f3fb
    ServiceAccountapigeeingressgatewaycicloudspanne660f3fb["ServiceAccount/apigee-ingressgateway-ci-cloud-spanne-660f3fb"]
    class ServiceAccountapigeeingressgatewaycicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeeingressgatewaycicloudspanne660f3fb
    ServiceAccountapigeemartcicloudspanne660f3fb["ServiceAccount/apigee-mart-ci-cloud-spanne-660f3fb"]
    class ServiceAccountapigeemartcicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeemartcicloudspanne660f3fb
    ServiceAccountapigeeruntimecicloudspannedevda008e1["ServiceAccount/apigee-runtime-ci-cloud-spanne-dev-da008e1"]
    class ServiceAccountapigeeruntimecicloudspannedevda008e1 primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeeruntimecicloudspannedevda008e1
    ServiceAccountapigeeudcacicloudspanne660f3fb["ServiceAccount/apigee-udca-ci-cloud-spanne-660f3fb"]
    class ServiceAccountapigeeudcacicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeeudcacicloudspanne660f3fb
    ServiceAccountapigeewatchercicloudspanne660f3fb["ServiceAccount/apigee-watcher-ci-cloud-spanne-660f3fb"]
    class ServiceAccountapigeewatchercicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeewatchercicloudspanne660f3fb
    Roleapigeecassandraschemavalcicloudspanne660f3fb["Role/apigee-cassandra-schema-val-ci-cloud-spanne-660f3fb"]
    class Roleapigeecassandraschemavalcicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> Roleapigeecassandraschemavalcicloudspanne660f3fb
    Roleapigeeingressgatewaycicloudspanne660f3fb["Role/apigee-ingressgateway-ci-cloud-spanne-660f3fb"]
    class Roleapigeeingressgatewaycicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> Roleapigeeingressgatewaycicloudspanne660f3fb
    Roleapigeewatchercicloudspanne660f3fb["Role/apigee-watcher-ci-cloud-spanne-660f3fb"]
    class Roleapigeewatchercicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> Roleapigeewatchercicloudspanne660f3fb
    RoleBindingapigeecassandraschemavalcicloudspanne660f3fb["RoleBinding/apigee-cassandra-schema-val-ci-cloud-spanne-660f3fb"]
    class RoleBindingapigeecassandraschemavalcicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> RoleBindingapigeecassandraschemavalcicloudspanne660f3fb
    RoleBindingapigeeingressgatewaycicloudspanne660f3fb["RoleBinding/apigee-ingressgateway-ci-cloud-spanne-660f3fb"]
    class RoleBindingapigeeingressgatewaycicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> RoleBindingapigeeingressgatewaycicloudspanne660f3fb
    RoleBindingapigeewatchercicloudspanne660f3fb["RoleBinding/apigee-watcher-ci-cloud-spanne-660f3fb"]
    class RoleBindingapigeewatchercicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> RoleBindingapigeewatchercicloudspanne660f3fb
    ApigeeDeploymentapigeeconnectagentcicloudspanne660f3fb["ApigeeDeployment/apigee-connect-agent-ci-cloud-spanne-660f3fb"]
    class ApigeeDeploymentapigeeconnectagentcicloudspanne660f3fb apigee_crd;
    ApigeeOrganizationcicloudspanne660f3fb --> ApigeeDeploymentapigeeconnectagentcicloudspanne660f3fb
    ApigeeDeploymentapigeeingressgatewayingresscicloudspanne660f3fb["ApigeeDeployment/apigee-ingressgateway-ingress-ci-cloud-spanne-660f3fb"]
    class ApigeeDeploymentapigeeingressgatewayingresscicloudspanne660f3fb apigee_crd;
    ApigeeOrganizationcicloudspanne660f3fb --> ApigeeDeploymentapigeeingressgatewayingresscicloudspanne660f3fb
    ApigeeDeploymentapigeeingressgatewayinternalchainingcicloudspanne660f3fb["ApigeeDeployment/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-660f3fb"]
    class ApigeeDeploymentapigeeingressgatewayinternalchainingcicloudspanne660f3fb apigee_crd;
    ApigeeOrganizationcicloudspanne660f3fb --> ApigeeDeploymentapigeeingressgatewayinternalchainingcicloudspanne660f3fb
    ApigeeDeploymentapigeemartcicloudspanne660f3fb["ApigeeDeployment/apigee-mart-ci-cloud-spanne-660f3fb"]
    class ApigeeDeploymentapigeemartcicloudspanne660f3fb apigee_crd;
    ApigeeOrganizationcicloudspanne660f3fb --> ApigeeDeploymentapigeemartcicloudspanne660f3fb
    ApigeeDeploymentapigeeudcacicloudspanne660f3fb["ApigeeDeployment/apigee-udca-ci-cloud-spanne-660f3fb"]
    class ApigeeDeploymentapigeeudcacicloudspanne660f3fb apigee_crd;
    ApigeeOrganizationcicloudspanne660f3fb --> ApigeeDeploymentapigeeudcacicloudspanne660f3fb
    ApigeeDeploymentapigeewatchercicloudspanne660f3fb["ApigeeDeployment/apigee-watcher-ci-cloud-spanne-660f3fb"]
    class ApigeeDeploymentapigeewatchercicloudspanne660f3fb apigee_crd;
    ApigeeOrganizationcicloudspanne660f3fb --> ApigeeDeploymentapigeewatchercicloudspanne660f3fb
    Certificateapigeecassandraschemasetupcicloudspanne660f3fb["Certificate/apigee-cassandra-schema-setup-ci-cloud-spanne-660f3fb"]
    class Certificateapigeecassandraschemasetupcicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> Certificateapigeecassandraschemasetupcicloudspanne660f3fb
    Certificateapigeecassandraschemavalcicloudspanne660f3fb["Certificate/apigee-cassandra-schema-val-ci-cloud-spanne-660f3fb"]
    class Certificateapigeecassandraschemavalcicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> Certificateapigeecassandraschemavalcicloudspanne660f3fb
    Certificateapigeecassandrausersetupcicloudspanne660f3fb["Certificate/apigee-cassandra-user-setup-ci-cloud-spanne-660f3fb"]
    class Certificateapigeecassandrausersetupcicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> Certificateapigeecassandrausersetupcicloudspanne660f3fb
    Certificateapigeeconnectagentcicloudspanne660f3fb["Certificate/apigee-connect-agent-ci-cloud-spanne-660f3fb"]
    class Certificateapigeeconnectagentcicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> Certificateapigeeconnectagentcicloudspanne660f3fb
    Certificateapigeemartcicloudspanne660f3fb["Certificate/apigee-mart-ci-cloud-spanne-660f3fb"]
    class Certificateapigeemartcicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> Certificateapigeemartcicloudspanne660f3fb
    Certificateapigeeudcacicloudspanne660f3fb["Certificate/apigee-udca-ci-cloud-spanne-660f3fb"]
    class Certificateapigeeudcacicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> Certificateapigeeudcacicloudspanne660f3fb
    Certificateapigeewatchercicloudspanne660f3fb["Certificate/apigee-watcher-ci-cloud-spanne-660f3fb"]
    class Certificateapigeewatchercicloudspanne660f3fb primitive;
    ApigeeOrganizationcicloudspanne660f3fb --> Certificateapigeewatchercicloudspanne660f3fb
    ReplicaSetapigeeconnectagentcicloudspanne660f3fb115023om3["ReplicaSet/apigee-connect-agent-ci-cloud-spanne-660f3fb-1150-23om3"]
    class ReplicaSetapigeeconnectagentcicloudspanne660f3fb115023om3 primitive;
    ApigeeDeploymentapigeeconnectagentcicloudspanne660f3fb --> ReplicaSetapigeeconnectagentcicloudspanne660f3fb115023om3
    Serviceapigeeconnectagentcicloudspanne660f3fb["Service/apigee-connect-agent-ci-cloud-spanne-660f3fb"]
    class Serviceapigeeconnectagentcicloudspanne660f3fb primitive;
    ApigeeDeploymentapigeeconnectagentcicloudspanne660f3fb --> Serviceapigeeconnectagentcicloudspanne660f3fb
    ReplicaSetapigeeingressgatewayingresscicloudspanne660f3fb1150gosr8["ReplicaSet/apigee-ingressgateway-ingress-ci-cloud-spanne-660f3fb-1150-gosr8"]
    class ReplicaSetapigeeingressgatewayingresscicloudspanne660f3fb1150gosr8 primitive;
    ApigeeDeploymentapigeeingressgatewayingresscicloudspanne660f3fb --> ReplicaSetapigeeingressgatewayingresscicloudspanne660f3fb1150gosr8
    Serviceapigeeingressgatewayingresscicloudspanne660f3fb["Service/apigee-ingressgateway-ingress-ci-cloud-spanne-660f3fb"]
    class Serviceapigeeingressgatewayingresscicloudspanne660f3fb primitive;
    ApigeeDeploymentapigeeingressgatewayingresscicloudspanne660f3fb --> Serviceapigeeingressgatewayingresscicloudspanne660f3fb
    ReplicaSetapigeeingressgatewayinternalchainingcicloudspanne660f3fb1150vtsph["ReplicaSet/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-660f3fb-1150-vtsph"]
    class ReplicaSetapigeeingressgatewayinternalchainingcicloudspanne660f3fb1150vtsph primitive;
    ApigeeDeploymentapigeeingressgatewayinternalchainingcicloudspanne660f3fb --> ReplicaSetapigeeingressgatewayinternalchainingcicloudspanne660f3fb1150vtsph
    Serviceapigeeingressgatewayinternalchainingcicloudspanne660f3fb["Service/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-660f3fb"]
    class Serviceapigeeingressgatewayinternalchainingcicloudspanne660f3fb primitive;
    ApigeeDeploymentapigeeingressgatewayinternalchainingcicloudspanne660f3fb --> Serviceapigeeingressgatewayinternalchainingcicloudspanne660f3fb
    ReplicaSetapigeemartcicloudspanne660f3fb1150im9ut["ReplicaSet/apigee-mart-ci-cloud-spanne-660f3fb-1150-im9ut"]
    class ReplicaSetapigeemartcicloudspanne660f3fb1150im9ut primitive;
    ApigeeDeploymentapigeemartcicloudspanne660f3fb --> ReplicaSetapigeemartcicloudspanne660f3fb1150im9ut
    Serviceapigeemartcicloudspanne660f3fb["Service/apigee-mart-ci-cloud-spanne-660f3fb"]
    class Serviceapigeemartcicloudspanne660f3fb primitive;
    ApigeeDeploymentapigeemartcicloudspanne660f3fb --> Serviceapigeemartcicloudspanne660f3fb
    ReplicaSetapigeeudcacicloudspanne660f3fb1150d2za3["ReplicaSet/apigee-udca-ci-cloud-spanne-660f3fb-1150-d2za3"]
    class ReplicaSetapigeeudcacicloudspanne660f3fb1150d2za3 primitive;
    ApigeeDeploymentapigeeudcacicloudspanne660f3fb --> ReplicaSetapigeeudcacicloudspanne660f3fb1150d2za3
    Serviceapigeeudcacicloudspanne660f3fb["Service/apigee-udca-ci-cloud-spanne-660f3fb"]
    class Serviceapigeeudcacicloudspanne660f3fb primitive;
    ApigeeDeploymentapigeeudcacicloudspanne660f3fb --> Serviceapigeeudcacicloudspanne660f3fb
    ReplicaSetapigeewatchercicloudspanne660f3fb1150s86b7["ReplicaSet/apigee-watcher-ci-cloud-spanne-660f3fb-1150-s86b7"]
    class ReplicaSetapigeewatchercicloudspanne660f3fb1150s86b7 primitive;
    ApigeeDeploymentapigeewatchercicloudspanne660f3fb --> ReplicaSetapigeewatchercicloudspanne660f3fb1150s86b7
    Serviceapigeewatchercicloudspanne660f3fb["Service/apigee-watcher-ci-cloud-spanne-660f3fb"]
    class Serviceapigeewatchercicloudspanne660f3fb primitive;
    ApigeeDeploymentapigeewatchercicloudspanne660f3fb --> Serviceapigeewatchercicloudspanne660f3fb
    Podapigeeconnectagentcicloudspanne660f3fb115023om36xcfn["Pod/apigee-connect-agent-ci-cloud-spanne-660f3fb-1150-23om3-6xcfn"]
    class Podapigeeconnectagentcicloudspanne660f3fb115023om36xcfn primitive;
    ReplicaSetapigeeconnectagentcicloudspanne660f3fb115023om3 --> Podapigeeconnectagentcicloudspanne660f3fb115023om36xcfn
    Podapigeeingressgatewayingresscicloudspanne660f3fb1150hlx5q["Pod/apigee-ingressgateway-ingress-ci-cloud-spanne-660f3fb-1150hlx5q"]
    class Podapigeeingressgatewayingresscicloudspanne660f3fb1150hlx5q primitive;
    ReplicaSetapigeeingressgatewayingresscicloudspanne660f3fb1150gosr8 --> Podapigeeingressgatewayingresscicloudspanne660f3fb1150hlx5q
    Podapigeeingressgatewayingresscicloudspanne660f3fb1150zgzh5["Pod/apigee-ingressgateway-ingress-ci-cloud-spanne-660f3fb-1150zgzh5"]
    class Podapigeeingressgatewayingresscicloudspanne660f3fb1150zgzh5 primitive;
    ReplicaSetapigeeingressgatewayingresscicloudspanne660f3fb1150gosr8 --> Podapigeeingressgatewayingresscicloudspanne660f3fb1150zgzh5
    Podapigeeingressgatewayinternalchainingcicloudspanne66mkpcd["Pod/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-66mkpcd"]
    class Podapigeeingressgatewayinternalchainingcicloudspanne66mkpcd primitive;
    ReplicaSetapigeeingressgatewayinternalchainingcicloudspanne660f3fb1150vtsph --> Podapigeeingressgatewayinternalchainingcicloudspanne66mkpcd
    Podapigeeingressgatewayinternalchainingcicloudspanne66q88hk["Pod/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-66q88hk"]
    class Podapigeeingressgatewayinternalchainingcicloudspanne66q88hk primitive;
    ReplicaSetapigeeingressgatewayinternalchainingcicloudspanne660f3fb1150vtsph --> Podapigeeingressgatewayinternalchainingcicloudspanne66q88hk
    Podapigeemartcicloudspanne660f3fb1150im9uttq496["Pod/apigee-mart-ci-cloud-spanne-660f3fb-1150-im9ut-tq496"]
    class Podapigeemartcicloudspanne660f3fb1150im9uttq496 primitive;
    ReplicaSetapigeemartcicloudspanne660f3fb1150im9ut --> Podapigeemartcicloudspanne660f3fb1150im9uttq496
    Podapigeeudcacicloudspanne660f3fb1150d2za3kdq5q["Pod/apigee-udca-ci-cloud-spanne-660f3fb-1150-d2za3-kdq5q"]
    class Podapigeeudcacicloudspanne660f3fb1150d2za3kdq5q primitive;
    ReplicaSetapigeeudcacicloudspanne660f3fb1150d2za3 --> Podapigeeudcacicloudspanne660f3fb1150d2za3kdq5q
    Podapigeewatchercicloudspanne660f3fb1150s86b7z44b9["Pod/apigee-watcher-ci-cloud-spanne-660f3fb-1150-s86b7-z44b9"]
    class Podapigeewatchercicloudspanne660f3fb1150s86b7z44b9 primitive;
    ReplicaSetapigeewatchercicloudspanne660f3fb1150s86b7 --> Podapigeewatchercicloudspanne660f3fb1150s86b7z44b9
    HelmReleasecicloudspannerc06d["Helm Release: ci-cloud-spanner-c06d"]
    class HelmReleasecicloudspannerc06d helm;
    Secretcicloudspanne660f3fbaxsalt["Secret/ci-cloud-spanne-660f3fb-ax-salt"]
    class Secretcicloudspanne660f3fbaxsalt primitive;
    HelmReleasecicloudspannerc06d --> Secretcicloudspanne660f3fbaxsalt
    Secretcicloudspanne660f3fbdataencryption["Secret/ci-cloud-spanne-660f3fb-data-encryption"]
    class Secretcicloudspanne660f3fbdataencryption primitive;
    HelmReleasecicloudspannerc06d --> Secretcicloudspanne660f3fbdataencryption
    Secretcicloudspanne660f3fbencryptionkeys["Secret/ci-cloud-spanne-660f3fb-encryption-keys"]
    class Secretcicloudspanne660f3fbencryptionkeys primitive;
    HelmReleasecicloudspannerc06d --> Secretcicloudspanne660f3fbencryptionkeys
    HelmReleasecicloudspannerc06d --> ApigeeOrganizationcicloudspanne660f3fb
    ApigeeRouteapigeeingressgatewayinternalchainingcicloudspanne660f3fb["ApigeeRoute/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-660f3fb"]
    class ApigeeRouteapigeeingressgatewayinternalchainingcicloudspanne660f3fb apigee_crd;
    HelmReleasecicloudspannerc06d --> ApigeeRouteapigeeingressgatewayinternalchainingcicloudspanne660f3fb
    Certificateapigeeingressgatewayinternalchainingcicloudspanne660f3fb["Certificate/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-660f3fb"]
    class Certificateapigeeingressgatewayinternalchainingcicloudspanne660f3fb primitive;
    HelmReleasecicloudspannerc06d --> Certificateapigeeingressgatewayinternalchainingcicloudspanne660f3fb
```
