Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'operator'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 33 related objects.
Building relationship map...
Generating Mermaid diagram...
#### Release operator -> Namespace apigee
```mermaid
graph TD;
    classDef helm fill:#f9f,stroke:#333,stroke-width:2px;
    classDef primitive fill:#d4edda,stroke:#155724,stroke-width:1px;
    classDef apigee_crd fill:#fff3cd,stroke:#856404,stroke-width:2px;
    Deploymentapigeecontrollermanager["Deployment/apigee-controller-manager"]
    class Deploymentapigeecontrollermanager primitive;
    ReplicaSetapigeecontrollermanager76fcc5456f["ReplicaSet/apigee-controller-manager-76fcc5456f"]
    class ReplicaSetapigeecontrollermanager76fcc5456f primitive;
    Deploymentapigeecontrollermanager --> ReplicaSetapigeecontrollermanager76fcc5456f
    Podapigeecontrollermanager76fcc5456ftq9pr["Pod/apigee-controller-manager-76fcc5456f-tq9pr"]
    class Podapigeecontrollermanager76fcc5456ftq9pr primitive;
    ReplicaSetapigeecontrollermanager76fcc5456f --> Podapigeecontrollermanager76fcc5456ftq9pr
    HelmReleaseoperator["Helm Release: operator"]
    class HelmReleaseoperator helm;
    HelmReleaseoperator --> Deploymentapigeecontrollermanager
    Serviceapigeecontrollermanagermetricsservice["Service/apigee-controller-manager-metrics-service"]
    class Serviceapigeecontrollermanagermetricsservice primitive;
    HelmReleaseoperator --> Serviceapigeecontrollermanagermetricsservice
    Serviceapigeewebhookservice["Service/apigee-webhook-service"]
    class Serviceapigeewebhookservice primitive;
    HelmReleaseoperator --> Serviceapigeewebhookservice
    ServiceAccountapigeemanager["ServiceAccount/apigee-manager"]
    class ServiceAccountapigeemanager primitive;
    HelmReleaseoperator --> ServiceAccountapigeemanager
    ServiceAccountapigeemetricsadapter["ServiceAccount/apigee-metrics-adapter"]
    class ServiceAccountapigeemetricsadapter primitive;
    HelmReleaseoperator --> ServiceAccountapigeemetricsadapter
    Roleapigeecassandrabackup["Role/apigee-cassandra-backup"]
    class Roleapigeecassandrabackup primitive;
    HelmReleaseoperator --> Roleapigeecassandrabackup
    Roleapigeecassandrarestore["Role/apigee-cassandra-restore"]
    class Roleapigeecassandrarestore primitive;
    HelmReleaseoperator --> Roleapigeecassandrarestore
    Roleapigeeingressgatewaymanagerapigee["Role/apigee-ingressgateway-manager-apigee"]
    class Roleapigeeingressgatewaymanagerapigee primitive;
    HelmReleaseoperator --> Roleapigeeingressgatewaymanagerapigee
    Roleapigeeingressgatewaysdsapigee["Role/apigee-ingressgateway-sds-apigee"]
    class Roleapigeeingressgatewaysdsapigee primitive;
    HelmReleaseoperator --> Roleapigeeingressgatewaysdsapigee
    Roleapigeeleaderelectionrole["Role/apigee-leader-election-role"]
    class Roleapigeeleaderelectionrole primitive;
    HelmReleaseoperator --> Roleapigeeleaderelectionrole
    Roleapigeemanagerrole["Role/apigee-manager-role"]
    class Roleapigeemanagerrole primitive;
    HelmReleaseoperator --> Roleapigeemanagerrole
    Roleapigeemetricsadapterapigeetelemetry["Role/apigee-metrics-adapter-apigee-telemetry"]
    class Roleapigeemetricsadapterapigeetelemetry primitive;
    HelmReleaseoperator --> Roleapigeemetricsadapterapigeetelemetry
    Rolewicredential["Role/wi-credential"]
    class Rolewicredential primitive;
    HelmReleaseoperator --> Rolewicredential
    RoleBindingapigeecassandrabackup["RoleBinding/apigee-cassandra-backup"]
    class RoleBindingapigeecassandrabackup primitive;
    HelmReleaseoperator --> RoleBindingapigeecassandrabackup
    RoleBindingapigeecassandrarestore["RoleBinding/apigee-cassandra-restore"]
    class RoleBindingapigeecassandrarestore primitive;
    HelmReleaseoperator --> RoleBindingapigeecassandrarestore
    RoleBindingapigeeingressgatewaymanagerapigee["RoleBinding/apigee-ingressgateway-manager-apigee"]
    class RoleBindingapigeeingressgatewaymanagerapigee primitive;
    HelmReleaseoperator --> RoleBindingapigeeingressgatewaymanagerapigee
    RoleBindingapigeeingressgatewaysdsapigee["RoleBinding/apigee-ingressgateway-sds-apigee"]
    class RoleBindingapigeeingressgatewaysdsapigee primitive;
    HelmReleaseoperator --> RoleBindingapigeeingressgatewaysdsapigee
    RoleBindingapigeeleaderelectionrolebinding["RoleBinding/apigee-leader-election-rolebinding"]
    class RoleBindingapigeeleaderelectionrolebinding primitive;
    HelmReleaseoperator --> RoleBindingapigeeleaderelectionrolebinding
    RoleBindingapigeemanagerrolebinding["RoleBinding/apigee-manager-rolebinding"]
    class RoleBindingapigeemanagerrolebinding primitive;
    HelmReleaseoperator --> RoleBindingapigeemanagerrolebinding
    RoleBindingapigeemetricsadapterapigeetelemetry["RoleBinding/apigee-metrics-adapter-apigee-telemetry"]
    class RoleBindingapigeemetricsadapterapigeetelemetry primitive;
    HelmReleaseoperator --> RoleBindingapigeemetricsadapterapigeetelemetry
    RoleBindingwicredential["RoleBinding/wi-credential"]
    class RoleBindingwicredential primitive;
    HelmReleaseoperator --> RoleBindingwicredential
    Certificateapigeeservingcert["Certificate/apigee-serving-cert"]
    class Certificateapigeeservingcert primitive;
    HelmReleaseoperator --> Certificateapigeeservingcert
    ClusterRoleapigeeingressgatewaymanagerapigee["ClusterRole/apigee-ingressgateway-manager-apigee"]
    class ClusterRoleapigeeingressgatewaymanagerapigee primitive;
    HelmReleaseoperator --> ClusterRoleapigeeingressgatewaymanagerapigee
    ClusterRoleapigeemanagerroleapigee["ClusterRole/apigee-manager-role-apigee"]
    class ClusterRoleapigeemanagerroleapigee primitive;
    HelmReleaseoperator --> ClusterRoleapigeemanagerroleapigee
    ClusterRoleapigeemetricsadapterapigeetelemetryapigee["ClusterRole/apigee-metrics-adapter-apigee-telemetry-apigee"]
    class ClusterRoleapigeemetricsadapterapigeetelemetryapigee primitive;
    HelmReleaseoperator --> ClusterRoleapigeemetricsadapterapigeetelemetryapigee
    ClusterRoleapigeeproxyroleapigee["ClusterRole/apigee-proxy-role-apigee"]
    class ClusterRoleapigeeproxyroleapigee primitive;
    HelmReleaseoperator --> ClusterRoleapigeeproxyroleapigee
    ClusterRoleBindingapigeeingressgatewaymanagerapigee["ClusterRoleBinding/apigee-ingressgateway-manager-apigee"]
    class ClusterRoleBindingapigeeingressgatewaymanagerapigee primitive;
    HelmReleaseoperator --> ClusterRoleBindingapigeeingressgatewaymanagerapigee
    ClusterRoleBindingapigeemanagerrolebindingapigee["ClusterRoleBinding/apigee-manager-rolebinding-apigee"]
    class ClusterRoleBindingapigeemanagerrolebindingapigee primitive;
    HelmReleaseoperator --> ClusterRoleBindingapigeemanagerrolebindingapigee
    ClusterRoleBindingapigeemetricsadapterapigeetelemetryapigee["ClusterRoleBinding/apigee-metrics-adapter-apigee-telemetry-apigee"]
    class ClusterRoleBindingapigeemetricsadapterapigeetelemetryapigee primitive;
    HelmReleaseoperator --> ClusterRoleBindingapigeemetricsadapterapigeetelemetryapigee
    ClusterRoleBindingapigeeproxyrolebindingapigee["ClusterRoleBinding/apigee-proxy-rolebinding-apigee"]
    class ClusterRoleBindingapigeeproxyrolebindingapigee primitive;
    HelmReleaseoperator --> ClusterRoleBindingapigeeproxyrolebindingapigee
    ClusterIssuerapigeecaissuer["ClusterIssuer/apigee-ca-issuer"]
    class ClusterIssuerapigeecaissuer primitive;
    HelmReleaseoperator --> ClusterIssuerapigeecaissuer
```
