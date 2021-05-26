# CCC-Assignment2
## Overview
The system deployed on Melbourne Research Cloud (MRC) can be access through link [http://172.26.131.90:8887/](http://172.26.131.90:8887/) (require VPN to access)



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
We created 4 different databases to store differnent for different scenario analysis.
  - all_twitter
  - beer_twitter
  - covid_twitter
  - income_twitter 
 - Grunt-couch is used to automatically deploy the design documents for different databases.
 - Mapreduce functions are used to remove repliaction and filter tweets.

## Twitter Harvest
We use twitter API to get data:
  - Stream API
  - User_timeline API
  - Search API

Each twitter harvester has been packaged as a docker image and pushed to dockerhub. 

## Twitter Analysis
The tiwtter analyzer is running in a docker container on the same MRC instance as a webserver.
The twitter analyzer uses couchDB cURL to communicate with couchDB and processes data to show in the frontend. 

## Webserver and visualization
The webserver is depolyed on one MRC instance. It loads data from the twitter analysis and show them in the web.

