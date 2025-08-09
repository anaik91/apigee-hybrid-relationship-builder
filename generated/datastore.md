Deep discovery enabled. Searching for all related objects.
Fetching all potential resources for deep discovery...
Identifying seed objects for release 'datastore'...
Starting recursive discovery from seed objects...

Discovery complete. Found a total of 8 related objects.
Building relationship map...
Generating Mermaid diagram...
#### Release datastore -> Namespace apigee
```mermaid
graph TD;
    classDef helm fill:#f9f,stroke:#333,stroke-width:2px;
    classDef primitive fill:#d4edda,stroke:#155724,stroke-width:1px;
    classDef apigee_crd fill:#fff3cd,stroke:#856404,stroke-width:2px;
    ApigeeDatastoredefault["ApigeeDatastore/default"]
    class ApigeeDatastoredefault apigee_crd;
    StatefulSetapigeecassandradefault["StatefulSet/apigee-cassandra-default"]
    class StatefulSetapigeecassandradefault primitive;
    ApigeeDatastoredefault --> StatefulSetapigeecassandradefault
    Serviceapigeecassandradefault["Service/apigee-cassandra-default"]
    class Serviceapigeecassandradefault primitive;
    ApigeeDatastoredefault --> Serviceapigeecassandradefault
    Secretconfigcassandradefault["Secret/config-cassandra-default"]
    class Secretconfigcassandradefault primitive;
    ApigeeDatastoredefault --> Secretconfigcassandradefault
    ServiceAccountapigeecassandradefault["ServiceAccount/apigee-cassandra-default"]
    class ServiceAccountapigeecassandradefault primitive;
    ApigeeDatastoredefault --> ServiceAccountapigeecassandradefault
    Certificateapigeecassandradefault["Certificate/apigee-cassandra-default"]
    class Certificateapigeecassandradefault primitive;
    ApigeeDatastoredefault --> Certificateapigeecassandradefault
    Podapigeecassandradefault0["Pod/apigee-cassandra-default-0"]
    class Podapigeecassandradefault0 primitive;
    StatefulSetapigeecassandradefault --> Podapigeecassandradefault0
    HelmReleasedatastore["Helm Release: datastore"]
    class HelmReleasedatastore helm;
    Secretapigeedatastoredefaultcreds["Secret/apigee-datastore-default-creds"]
    class Secretapigeedatastoredefaultcreds primitive;
    HelmReleasedatastore --> Secretapigeedatastoredefaultcreds
    HelmReleasedatastore --> ApigeeDatastoredefault
```
