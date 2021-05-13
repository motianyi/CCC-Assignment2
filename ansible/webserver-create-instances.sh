#!/bin/bash

sudo . ./unimelb-comp90024-2021-grp-31-openrc.sh

# Create flask web server
ansible-playbook webserver-create-instances.yaml

# Install Dependency, set up proxy
ansible-playbook install-dep.yaml -i inventory/inventory_webserver_file.ini