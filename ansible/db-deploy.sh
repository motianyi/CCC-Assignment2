#!/bin/bash

# install dependency and docker, then set up couchDB cluster
ansible-playbook db-deploy.yaml -i inventory/inventory_file.ini
