#!/bin/bash

# create couchDB instance
sudo . ./unimelb-comp90024-2021-grp-31-openrc.sh; ansible-playbook create-instances.yaml

# install dependency and docker, then set up couchDB cluster
ansible-playbook db-deploy.yaml -i inventory/inventory_file.ini
