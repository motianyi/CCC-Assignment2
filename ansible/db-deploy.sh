#!/bin/bash

# install dependency and docker, then set up couchDB cluster
# require sudo because it will install npm on localhost
sudo ansible-playbook db-deploy.yaml -i inventory/inventory_file.ini
