#!/bin/bash

# Install Dependency, set up proxy, run image
ansible-playbook webserver-deploy.yaml -i inventory/inventory_webserver_file.ini