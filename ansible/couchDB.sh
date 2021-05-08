#!/bin/bash

. ./unimelb-comp90024-2021-grp-31-openrc.sh; ansible-playbook couchDB.yaml -i inventory/inventory_file.ini
