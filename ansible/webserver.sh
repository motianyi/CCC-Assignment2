#!/bin/bash

# Create flask web server instance
sudo . ./unimelb-comp90024-2021-grp-31-openrc.sh; ansible-playbook webserver-create-instances.yaml

# Install Dependency, set up proxy, run image
ansible-playbook webserver-deploy.yaml -i inventory/inventory_webserver_file.ini