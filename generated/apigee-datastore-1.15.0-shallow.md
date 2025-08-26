Deep discovery disabled. Searching for Helm-managed objects only.
Fetching all potential resources for shallow discovery...
Identifying objects directly managed by release 'datastore'...

Discovery complete. Found a total of 4 related objects.
Applying filters to discovered objects...
Filters applied. 4 objects remaining for diagram.
Building relationship map...
Generating Mermaid diagram with color-coded kinds...

#### Release: datastore | Namespace: apigee
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

    HelmReleasedatastore["Helm Release: datastore"]
    Secretapigeedatastoredefaultcreds["Secret/apigee-datastore-default-creds"]
    ServiceAccountapigeecassandrabackupsa["ServiceAccount/apigee-cassandra-backup-sa"]
    Certificateapigeecassandrabackuptls["Certificate/apigee-cassandra-backup-tls"]
    ApigeeDatastoredefault["ApigeeDatastore/default"]

    class HelmReleasedatastore helm;
    class Secretapigeedatastoredefaultcreds config;
    class ServiceAccountapigeecassandrabackupsa rbac;
    class Certificateapigeecassandrabackuptls cert_manager_crd;
    class ApigeeDatastoredefault apigee_crd;

    HelmReleasedatastore --> Secretapigeedatastoredefaultcreds
    HelmReleasedatastore --> ServiceAccountapigeecassandrabackupsa
    HelmReleasedatastore --> Certificateapigeecassandrabackuptls
    HelmReleasedatastore --> ApigeeDatastoredefault
```
