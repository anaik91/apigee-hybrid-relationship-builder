#!/bin/bash

APIGEE_NS="apigee"
GEN_DIR="generated"
mkdir "$GEN_DIR"
for helm_release in $(helm ls -n apigee -q)
do
    echo "Generating deep discovery for release => $helm_release"
    python3 generate_apigee_map.py \
        -n "$APIGEE_NS" \
        "$helm_release" \
        --md-format \
        --deep-discovery \
        --exclude-kinds Role RoleBinding ClusterRole ClusterRoleBinding > "$GEN_DIR/$helm_release-deep.md"
        
    echo "Generating shallow discovery for release => $helm_release"
    python3 generate_apigee_map.py \
        -n "$APIGEE_NS" \
        "$helm_release" \
        --md-format \
        --exclude-kinds Role RoleBinding ClusterRole ClusterRoleBinding > "$GEN_DIR/$helm_release-shallow.md"
done