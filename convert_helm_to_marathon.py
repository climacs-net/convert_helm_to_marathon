import tarfile
import yaml
import json
import os

# Extract the Helm chart tarball
def extract_tgz(tar_path, extract_path):
    with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=extract_path)

# Convert values.yaml to Marathon JSON
def convert_values_to_marathon(values_path, output_path):
    with open(values_path, 'r') as f:
        values = yaml.safe_load(f)

    marathon_json = {
        "id": "nginx",
        "cmd": None,
        "cpus": 0.5,
        "mem": 512,
        "instances": values['replicaCount'],
        "container": {
            "type": "DOCKER",
            "docker": {
                "image": f"{values['image']['repository']}:{values['image']['tag']}",
                "network": "BRIDGE",
                "portMappings": [
                    {
                        "containerPort": values['service']['port'],
                        "hostPort": 0,
                        "servicePort": 10000,
                        "protocol": "tcp"
                    }
                ]
            }
        },
        "labels": {
            "HAPROXY_GROUP": "external"
        },
        "portDefinitions": [
            {
                "port": 10000,
                "protocol": "tcp",
                "labels": {}
            }
        ]
    }

    with open(output_path, 'w') as f:
        json.dump(marathon_json, f, indent=2)

# Re-package the files into a new tarball
def create_tgz(output_tgz, files):
    with tarfile.open(output_tgz, "w:gz") as tar:
        for file in files:
            tar.add(file, arcname=os.path.basename(file))

# Main function
def main():
    input_tgz = 'ingress-nginx-4.0.6.tgz'
    extract_path = 'extracted_chart'
    values_file = os.path.join(extract_path, 'ingress-nginx', 'values.yaml')
    output_json = 'marathon.json'
    output_tgz = 'converted_chart.tgz'

    # Step 1: Extract the tarball
    extract_tgz(input_tgz, extract_path)

    # Step 2: Convert values.yaml to Marathon JSON
    convert_values_to_marathon(values_file, output_json)

    # Step 3: Create a new tarball with the converted Marathon JSON
    create_tgz(output_tgz, [output_json])

if __name__ == "__main__":
    main()
