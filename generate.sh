#!/bin/bash

APIGEE_NS="apigee"
GEN_DIR="generated"
mkdir "$GEN_DIR"
for helm_release in $(helm ls -n apigee -q)
do
    echo "Generating Map for release => $helm_release"
    python3 generate_apigee_map.py \
        -n "$APIGEE_NS" \
        "$helm_release" \
        --md-format \
        --deep-discovery > "$GEN_DIR/$helm_release.md"
done