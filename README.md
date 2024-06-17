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
- **50 GB SSD**
- **8 GB RAM**
- **Elastic IP**
- **Fully Qualified Domain Names (FQDN)**:
  - Bamboo: `bamboodemo.climacs.net`
  - Nexus: `nexusdemo.climacs.net`

## Setup Instructions

### Server Creation (via Terraform)

1. Clone the repository:
   ```bash
   git clone https://github.com/climacs-net/convert_helm_to_marathon.git
   cd convert_helm_to_marathon
