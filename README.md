# CCC-Assignment2
## Overview
The system deployed on Melbourne Research Cloud (MRC) can be access through link [http://172.26.131.90:8887/](http://172.26.131.90:8887/) (requires VPN to access)

## File Directories


## Usage
The whole sysetem consists of webserver, couchdb database and data harvester. In order to deploy the whole system on the Melbouren Research Cloud (MRC). Before deploy the system, you need to download the OpenStack RC File from the MRC Dashboard and get your user password. This file contains the Environment variables that are necessary to run OpenStack command-line clients.
- Make sure you have OpenStack RC File and password
- Make sure you have connected to unimelb network or connect to the VPN 

If you want to create and deploy all parts of the system, you can execute the following command from the ```ansible``` directory. 
```bash
cd ansible
sh ./deployall.sh
```
The following showed the command will run in ```deployall.sh```. In some occasions, for example if the instance is already created, you can run commands to do spcific tasks.
```bash
#!/bin/bash

# Creating instances for database and harvesters
sh ./db-create-instances.sh

# Deploy couchDB database cluster
sh ./db-deploy.sh

# Deploy twitter harvester
sh ./harvester-deploy.sh

# Creating instances for webserver and data analyzer
sh ./webserver-create-instances.sh

# Deploy the webserver and data analyzer
sh ./webserver-deploy.sh
```
All details of deployment of this system can be found at [ansible directory](ansible/README.md).
## CouchDB

## Tiwtter Harvest
