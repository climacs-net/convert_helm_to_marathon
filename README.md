# Helm to Marathon Conversion

This repository contains the code to convert Helm charts to Marathon configuration using Python. The repository includes YAML files for setting up a pipeline and necessary Ansible playbooks for setting up Bamboo and Nexus servers.

## Table of Contents

- [Infrastructure](#infrastructure)
- [Setup Instructions](#setup-instructions)
- [Pipeline Workflow](#pipeline-workflow)
- [Cost](#cost)

## Infrastructure

The infrastructure for this project is provisioned using Terraform. The setup includes two servers (Bamboo and Nexus) with the following specifications:

- **AWS t3.large instance (2 cores)**
  - 50 GB SSD
  - 8 GB RAM
  - Elastic IP
  - Fully Qualified Domain Names (FQDN):
    - Bamboo: `bamboodemo.climacs.net`

- **Nexus Server**:
  - AWS t3.medium instance (2 cores)
  - 50 GB SSD
  - 4 GB RAM
  - Elastic IP
  - Fully Qualified Domain Name (FQDN): 
    - Nexus: `nexusdemo.climacs.net`

## Setup Instructions

### Server Creation (via Terraform)
   
1. Clone the repository:
   ```bash
   git clone https://github.com/climacs-net/convert_helm_to_marathon.git
   cd convert_helm_to_marathon

2. Initialize and apply the Terraform configuration:
   ```bash
   terraform init
   terraform apply

3. Run the Ansible playbook for Bamboo installation:
   ```bash
   ansible-playbook -i inventory bamboo_playbook.yml

4. Run the Ansible playbook for Nexus installation:
   ```bash
   ansible-playbook -i inventory nexus_playbook.yml 


## Pipeline Workflow

The pipeline is defined in a YAML file and involves the following steps:

1. **GitHub**: https://github.com/climacs-net/convert_helm_to_marathon
2. **Conversion**: Convert tar-ball-gz ingress-nginx to Marathon.
3. **Compression**: Compress the Marathon JSON file to tar.gz.
4. **Upload**: Upload the tar.gz to Nexus.

### Pipeline Setup

1. Ensure your source repository on GitHub contains the necessary code for conversion.
2. Configure the pipeline YAML file according to your environment and requirements.
3. Execute the pipeline to automate the conversion and upload process.

## Cost

The running servers cost approximately $4 to $4.5 per day.


