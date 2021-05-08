#!/bin/bash
chmod 755 ./inventory
. ./unimelb-comp90024-2021-grp-31-openrc.sh; ansible-playbook create-instances.yaml