Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'ci-cloud-spanner-c06d'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 57 related objects.
Filters applied. 51 objects remaining for diagram.
Building relationship map...
Generating Mermaid diagram with color-coded kinds...

#### Release: ci-cloud-spanner-c06d | Namespace: apigee
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

    ApigeeOrganizationcicloudspanne660f3fb["ApigeeOrganization/ci-cloud-spanne-660f3fb"]
    ConfigMapapigeecassandraschemavalcicloudspanne660f3fb["ConfigMap/apigee-cassandra-schema-val-ci-cloud-spanne-660f3fb"]
    ConfigMapapigeeudcacicloudspanne660f3fbfluentdconfig["ConfigMap/apigee-udca-ci-cloud-spanne-660f3fb-fluentd-config"]
    Secretapigeemartcicloudspanne660f3fbconfig1a6a79["Secret/apigee-mart-ci-cloud-spanne-660f3fb-config-1a6a79"]
    ServiceAccountapigeecassandraschemasetupcicloudspanne660f3fb["ServiceAccount/apigee-cassandra-schema-setup-ci-cloud-spanne-660f3fb"]
    ServiceAccountapigeecassandraschemavalcicloudspanne660f3fb["ServiceAccount/apigee-cassandra-schema-val-ci-cloud-spanne-660f3fb"]
    ServiceAccountapigeecassandrausersetupcicloudspanne660f3fb["ServiceAccount/apigee-cassandra-user-setup-ci-cloud-spanne-660f3fb"]
    ServiceAccountapigeeconnectagentcicloudspanne660f3fb["ServiceAccount/apigee-connect-agent-ci-cloud-spanne-660f3fb"]
    ServiceAccountapigeeingressgatewaycicloudspanne660f3fb["ServiceAccount/apigee-ingressgateway-ci-cloud-spanne-660f3fb"]
    ServiceAccountapigeemartcicloudspanne660f3fb["ServiceAccount/apigee-mart-ci-cloud-spanne-660f3fb"]
    ServiceAccountapigeeruntimecicloudspannedevda008e1["ServiceAccount/apigee-runtime-ci-cloud-spanne-dev-da008e1"]
    ServiceAccountapigeeudcacicloudspanne660f3fb["ServiceAccount/apigee-udca-ci-cloud-spanne-660f3fb"]
    ServiceAccountapigeewatchercicloudspanne660f3fb["ServiceAccount/apigee-watcher-ci-cloud-spanne-660f3fb"]
    Certificateapigeecassandraschemasetupcicloudspanne660f3fb["Certificate/apigee-cassandra-schema-setup-ci-cloud-spanne-660f3fb"]
    Certificateapigeecassandraschemavalcicloudspanne660f3fb["Certificate/apigee-cassandra-schema-val-ci-cloud-spanne-660f3fb"]
    Certificateapigeecassandrausersetupcicloudspanne660f3fb["Certificate/apigee-cassandra-user-setup-ci-cloud-spanne-660f3fb"]
    Certificateapigeeconnectagentcicloudspanne660f3fb["Certificate/apigee-connect-agent-ci-cloud-spanne-660f3fb"]
    Certificateapigeemartcicloudspanne660f3fb["Certificate/apigee-mart-ci-cloud-spanne-660f3fb"]
    Certificateapigeeudcacicloudspanne660f3fb["Certificate/apigee-udca-ci-cloud-spanne-660f3fb"]
    Certificateapigeewatchercicloudspanne660f3fb["Certificate/apigee-watcher-ci-cloud-spanne-660f3fb"]
    ApigeeDeploymentapigeeconnectagentcicloudspanne660f3fb["ApigeeDeployment/apigee-connect-agent-ci-cloud-spanne-660f3fb"]
    ApigeeDeploymentapigeeingressgatewayingresscicloudspanne660f3fb["ApigeeDeployment/apigee-ingressgateway-ingress-ci-cloud-spanne-660f3fb"]
    ApigeeDeploymentapigeeingressgatewayinternalchainingcicloudspanne660f3fb["ApigeeDeployment/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-660f3fb"]
    ApigeeDeploymentapigeemartcicloudspanne660f3fb["ApigeeDeployment/apigee-mart-ci-cloud-spanne-660f3fb"]
    ApigeeDeploymentapigeeudcacicloudspanne660f3fb["ApigeeDeployment/apigee-udca-ci-cloud-spanne-660f3fb"]
    ApigeeDeploymentapigeewatchercicloudspanne660f3fb["ApigeeDeployment/apigee-watcher-ci-cloud-spanne-660f3fb"]
    ReplicaSetapigeeconnectagentcicloudspanne660f3fb115023om3["ReplicaSet/apigee-connect-agent-ci-cloud-spanne-660f3fb-1150-23om3"]
    Serviceapigeeconnectagentcicloudspanne660f3fb["Service/apigee-connect-agent-ci-cloud-spanne-660f3fb"]
    ReplicaSetapigeeingressgatewayingresscicloudspanne660f3fb1150gosr8["ReplicaSet/apigee-ingressgateway-ingress-ci-cloud-spanne-660f3fb-1150-gosr8"]
    Serviceapigeeingressgatewayingresscicloudspanne660f3fb["Service/apigee-ingressgateway-ingress-ci-cloud-spanne-660f3fb"]
    ReplicaSetapigeeingressgatewayinternalchainingcicloudspanne660f3fb1150vtsph["ReplicaSet/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-660f3fb-1150-vtsph"]
    Serviceapigeeingressgatewayinternalchainingcicloudspanne660f3fb["Service/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-660f3fb"]
    ReplicaSetapigeemartcicloudspanne660f3fb1150im9ut["ReplicaSet/apigee-mart-ci-cloud-spanne-660f3fb-1150-im9ut"]
    Serviceapigeemartcicloudspanne660f3fb["Service/apigee-mart-ci-cloud-spanne-660f3fb"]
    ReplicaSetapigeeudcacicloudspanne660f3fb1150d2za3["ReplicaSet/apigee-udca-ci-cloud-spanne-660f3fb-1150-d2za3"]
    Serviceapigeeudcacicloudspanne660f3fb["Service/apigee-udca-ci-cloud-spanne-660f3fb"]
    ReplicaSetapigeewatchercicloudspanne660f3fb1150s86b7["ReplicaSet/apigee-watcher-ci-cloud-spanne-660f3fb-1150-s86b7"]
    Serviceapigeewatchercicloudspanne660f3fb["Service/apigee-watcher-ci-cloud-spanne-660f3fb"]
    Podapigeeconnectagentcicloudspanne660f3fb115023om36xcfn["Pod/apigee-connect-agent-ci-cloud-spanne-660f3fb-1150-23om3-6xcfn"]
    Podapigeeingressgatewayingresscicloudspanne660f3fb1150hlx5q["Pod/apigee-ingressgateway-ingress-ci-cloud-spanne-660f3fb-1150hlx5q"]
    Podapigeeingressgatewayingresscicloudspanne660f3fb1150zgzh5["Pod/apigee-ingressgateway-ingress-ci-cloud-spanne-660f3fb-1150zgzh5"]
    Podapigeeingressgatewayinternalchainingcicloudspanne66mkpcd["Pod/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-66mkpcd"]
    Podapigeeingressgatewayinternalchainingcicloudspanne66q88hk["Pod/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-66q88hk"]
    Podapigeemartcicloudspanne660f3fb1150im9uttq496["Pod/apigee-mart-ci-cloud-spanne-660f3fb-1150-im9ut-tq496"]
    Podapigeeudcacicloudspanne660f3fb1150d2za3kdq5q["Pod/apigee-udca-ci-cloud-spanne-660f3fb-1150-d2za3-kdq5q"]
    Podapigeewatchercicloudspanne660f3fb1150s86b7z44b9["Pod/apigee-watcher-ci-cloud-spanne-660f3fb-1150-s86b7-z44b9"]
    HelmReleasecicloudspannerc06d["Helm Release: ci-cloud-spanner-c06d"]
    Secretcicloudspanne660f3fbaxsalt["Secret/ci-cloud-spanne-660f3fb-ax-salt"]
    Secretcicloudspanne660f3fbdataencryption["Secret/ci-cloud-spanne-660f3fb-data-encryption"]
    Secretcicloudspanne660f3fbencryptionkeys["Secret/ci-cloud-spanne-660f3fb-encryption-keys"]
    Certificateapigeeingressgatewayinternalchainingcicloudspanne660f3fb["Certificate/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-660f3fb"]
    ApigeeRouteapigeeingressgatewayinternalchainingcicloudspanne660f3fb["ApigeeRoute/apigee-ingressgateway-internal-chaining-ci-cloud-spanne-660f3fb"]

    class ApigeeOrganizationcicloudspanne660f3fb apigee_crd;
    class ConfigMapapigeecassandraschemavalcicloudspanne660f3fb config;
    class ConfigMapapigeeudcacicloudspanne660f3fbfluentdconfig config;
    class Secretapigeemartcicloudspanne660f3fbconfig1a6a79 config;
    class ServiceAccountapigeecassandraschemasetupcicloudspanne660f3fb rbac;
    class ServiceAccountapigeecassandraschemavalcicloudspanne660f3fb rbac;
    class ServiceAccountapigeecassandrausersetupcicloudspanne660f3fb rbac;
    class ServiceAccountapigeeconnectagentcicloudspanne660f3fb rbac;
    class ServiceAccountapigeeingressgatewaycicloudspanne660f3fb rbac;
    class ServiceAccountapigeemartcicloudspanne660f3fb rbac;
    class ServiceAccountapigeeruntimecicloudspannedevda008e1 rbac;
    class ServiceAccountapigeeudcacicloudspanne660f3fb rbac;
    class ServiceAccountapigeewatchercicloudspanne660f3fb rbac;
    class Certificateapigeecassandraschemasetupcicloudspanne660f3fb cert_manager_crd;
    class Certificateapigeecassandraschemavalcicloudspanne660f3fb cert_manager_crd;
    class Certificateapigeecassandrausersetupcicloudspanne660f3fb cert_manager_crd;
    class Certificateapigeeconnectagentcicloudspanne660f3fb cert_manager_crd;
    class Certificateapigeemartcicloudspanne660f3fb cert_manager_crd;
    class Certificateapigeeudcacicloudspanne660f3fb cert_manager_crd;
    class Certificateapigeewatchercicloudspanne660f3fb cert_manager_crd;
    class ApigeeDeploymentapigeeconnectagentcicloudspanne660f3fb apigee_crd;
    class ApigeeDeploymentapigeeingressgatewayingresscicloudspanne660f3fb apigee_crd;
    class ApigeeDeploymentapigeeingressgatewayinternalchainingcicloudspanne660f3fb apigee_crd;
    class ApigeeDeploymentapigeemartcicloudspanne660f3fb apigee_crd;
    class ApigeeDeploymentapigeeudcacicloudspanne660f3fb apigee_crd;
    class ApigeeDeploymentapigeewatchercicloudspanne660f3fb apigee_crd;
    class ReplicaSetapigeeconnectagentcicloudspanne660f3fb115023om3 workload;
    class Serviceapigeeconnectagentcicloudspanne660f3fb network;
    class ReplicaSetapigeeingressgatewayingresscicloudspanne660f3fb1150gosr8 workload;
    class Serviceapigeeingressgatewayingresscicloudspanne660f3fb network;
    class ReplicaSetapigeeingressgatewayinternalchainingcicloudspanne660f3fb1150vtsph workload;
    class Serviceapigeeingressgatewayinternalchainingcicloudspanne660f3fb network;
    class ReplicaSetapigeemartcicloudspanne660f3fb1150im9ut workload;
    class Serviceapigeemartcicloudspanne660f3fb network;
    class ReplicaSetapigeeudcacicloudspanne660f3fb1150d2za3 workload;
    class Serviceapigeeudcacicloudspanne660f3fb network;
    class ReplicaSetapigeewatchercicloudspanne660f3fb1150s86b7 workload;
    class Serviceapigeewatchercicloudspanne660f3fb network;
    class Podapigeeconnectagentcicloudspanne660f3fb115023om36xcfn workload;
    class Podapigeeingressgatewayingresscicloudspanne660f3fb1150hlx5q workload;
    class Podapigeeingressgatewayingresscicloudspanne660f3fb1150zgzh5 workload;
    class Podapigeeingressgatewayinternalchainingcicloudspanne66mkpcd workload;
    class Podapigeeingressgatewayinternalchainingcicloudspanne66q88hk workload;
    class Podapigeemartcicloudspanne660f3fb1150im9uttq496 workload;
    class Podapigeeudcacicloudspanne660f3fb1150d2za3kdq5q workload;
    class Podapigeewatchercicloudspanne660f3fb1150s86b7z44b9 workload;
    class HelmReleasecicloudspannerc06d helm;
    class Secretcicloudspanne660f3fbaxsalt config;
    class Secretcicloudspanne660f3fbdataencryption config;
    class Secretcicloudspanne660f3fbencryptionkeys config;
    class Certificateapigeeingressgatewayinternalchainingcicloudspanne660f3fb cert_manager_crd;
    class ApigeeRouteapigeeingressgatewayinternalchainingcicloudspanne660f3fb apigee_crd;

    ApigeeOrganizationcicloudspanne660f3fb --> ConfigMapapigeecassandraschemavalcicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> ConfigMapapigeeudcacicloudspanne660f3fbfluentdconfig
    ApigeeOrganizationcicloudspanne660f3fb --> Secretapigeemartcicloudspanne660f3fbconfig1a6a79
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeecassandraschemasetupcicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeecassandraschemavalcicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeecassandrausersetupcicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeeconnectagentcicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeeingressgatewaycicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeemartcicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeeruntimecicloudspannedevda008e1
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeeudcacicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> ServiceAccountapigeewatchercicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> Certificateapigeecassandraschemasetupcicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> Certificateapigeecassandraschemavalcicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> Certificateapigeecassandrausersetupcicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> Certificateapigeeconnectagentcicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> Certificateapigeemartcicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> Certificateapigeeudcacicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> Certificateapigeewatchercicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> ApigeeDeploymentapigeeconnectagentcicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> ApigeeDeploymentapigeeingressgatewayingresscicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> ApigeeDeploymentapigeeingressgatewayinternalchainingcicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> ApigeeDeploymentapigeemartcicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> ApigeeDeploymentapigeeudcacicloudspanne660f3fb
    ApigeeOrganizationcicloudspanne660f3fb --> ApigeeDeploymentapigeewatchercicloudspanne660f3fb
    ApigeeDeploymentapigeeconnectagentcicloudspanne660f3fb --> ReplicaSetapigeeconnectagentcicloudspanne660f3fb115023om3
    ApigeeDeploymentapigeeconnectagentcicloudspanne660f3fb --> Serviceapigeeconnectagentcicloudspanne660f3fb
    ApigeeDeploymentapigeeingressgatewayingresscicloudspanne660f3fb --> ReplicaSetapigeeingressgatewayingresscicloudspanne660f3fb1150gosr8
    ApigeeDeploymentapigeeingressgatewayingresscicloudspanne660f3fb --> Serviceapigeeingressgatewayingresscicloudspanne660f3fb
    ApigeeDeploymentapigeeingressgatewayinternalchainingcicloudspanne660f3fb --> ReplicaSetapigeeingressgatewayinternalchainingcicloudspanne660f3fb1150vtsph
    ApigeeDeploymentapigeeingressgatewayinternalchainingcicloudspanne660f3fb --> Serviceapigeeingressgatewayinternalchainingcicloudspanne660f3fb
    ApigeeDeploymentapigeemartcicloudspanne660f3fb --> ReplicaSetapigeemartcicloudspanne660f3fb1150im9ut
    ApigeeDeploymentapigeemartcicloudspanne660f3fb --> Serviceapigeemartcicloudspanne660f3fb
    ApigeeDeploymentapigeeudcacicloudspanne660f3fb --> ReplicaSetapigeeudcacicloudspanne660f3fb1150d2za3
    ApigeeDeploymentapigeeudcacicloudspanne660f3fb --> Serviceapigeeudcacicloudspanne660f3fb
    ApigeeDeploymentapigeewatchercicloudspanne660f3fb --> ReplicaSetapigeewatchercicloudspanne660f3fb1150s86b7
    ApigeeDeploymentapigeewatchercicloudspanne660f3fb --> Serviceapigeewatchercicloudspanne660f3fb
    ReplicaSetapigeeconnectagentcicloudspanne660f3fb115023om3 --> Podapigeeconnectagentcicloudspanne660f3fb115023om36xcfn
    ReplicaSetapigeeingressgatewayingresscicloudspanne660f3fb1150gosr8 --> Podapigeeingressgatewayingresscicloudspanne660f3fb1150hlx5q
    ReplicaSetapigeeingressgatewayingresscicloudspanne660f3fb1150gosr8 --> Podapigeeingressgatewayingresscicloudspanne660f3fb1150zgzh5
    ReplicaSetapigeeingressgatewayinternalchainingcicloudspanne660f3fb1150vtsph --> Podapigeeingressgatewayinternalchainingcicloudspanne66mkpcd
    ReplicaSetapigeeingressgatewayinternalchainingcicloudspanne660f3fb1150vtsph --> Podapigeeingressgatewayinternalchainingcicloudspanne66q88hk
    ReplicaSetapigeemartcicloudspanne660f3fb1150im9ut --> Podapigeemartcicloudspanne660f3fb1150im9uttq496
    ReplicaSetapigeeudcacicloudspanne660f3fb1150d2za3 --> Podapigeeudcacicloudspanne660f3fb1150d2za3kdq5q
    ReplicaSetapigeewatchercicloudspanne660f3fb1150s86b7 --> Podapigeewatchercicloudspanne660f3fb1150s86b7z44b9
    HelmReleasecicloudspannerc06d --> Secretcicloudspanne660f3fbaxsalt
    HelmReleasecicloudspannerc06d --> Secretcicloudspanne660f3fbdataencryption
    HelmReleasecicloudspannerc06d --> Secretcicloudspanne660f3fbencryptionkeys
    HelmReleasecicloudspannerc06d --> Certificateapigeeingressgatewayinternalchainingcicloudspanne660f3fb
    HelmReleasecicloudspannerc06d --> ApigeeOrganizationcicloudspanne660f3fb
    HelmReleasecicloudspannerc06d --> ApigeeRouteapigeeingressgatewayinternalchainingcicloudspanne660f3fb
```
