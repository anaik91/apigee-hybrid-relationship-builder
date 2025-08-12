#!/bin/bash

APIGEE_NS="apigee"
GEN_DIR="generated"
mkdir "$GEN_DIR"
mkdir "$GEN_DIR/svg"

for helm_release in $(helm ls -n apigee -q)
do
    chart_name=$(helm ls -n apigee -o json | jq --arg helm_release "$helm_release" -r '.[] | select(.name == $helm_release) | .chart')
    echo "Generating deep discovery for release => $helm_release | chart_name => $chart_name"
    python3 generate_apigee_map.py \
        -n "$APIGEE_NS" \
        "$helm_release" \
        --md-format \
        --deep-discovery \
        --exclude-kinds Role RoleBinding ClusterRole ClusterRoleBinding > "$GEN_DIR/$chart_name-deep.md"
    # mmdc : https://github.com/mermaid-js/mermaid-cli
    mmdc -i "$GEN_DIR/$chart_name-deep.md" -o "$GEN_DIR/svg/$chart_name-deep.svg"
    echo "Generating shallow discovery for release => $helm_release | chart_name => $chart_name"
    python3 generate_apigee_map.py \
        -n "$APIGEE_NS" \
        "$helm_release" \
        --md-format \
        --exclude-kinds Role RoleBinding ClusterRole ClusterRoleBinding > "$GEN_DIR/$chart_name-shallow.md"
    # mmdc : https://github.com/mermaid-js/mermaid-cli
    mmdc -i "$GEN_DIR/$chart_name-shallow.md" -o "$GEN_DIR/svg/$chart_name-shallow.svg"
done