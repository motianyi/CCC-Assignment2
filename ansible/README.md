# Deployment the system using ansible

The whole sysetem consists of webserver, couchdb database and data harvester. In order to deploy the whole system on the Melbouren Research Cloud (MRC). Before deploy the system, you need to download the OpenStack RC File from the MRC Dashboard and get your user password. This file contains the Environment variables that are necessary to run OpenStack command-line clients.
- Make sure you have OpenStack RC File and password
- Make sure you have connected to unimelb network or connect to the VPN 

If you want to create and deploy all parts of the system, you can execute the following command from the ```ansible``` directory. 
```bash
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

# Description of each task
## 1. Creating instances for database and harvesters
This taks will execute ```db-create-instances.yaml``` palybook which consists of four roles
-   openstack-volume : 
    -   Creating the volumns used for each instances
-   openstack-security-group
    -   Set up the security rules for the instances
-   openstack-instance
    -   Create the instance for the CouchDB database cluster and the Twitter Harvesters, under current configuration, it will create 2 instances. The harvester and CouchDB will be deployed on each of these two instances.
    -   The task create instances with volumes attached, it will also add the ip-address of created instances into in-memory inventory.
-   save-ip: 
    -   The ip address will be automatically saved in ```inventory/inventory_file.ini```. The file can be used in subsequent tasks to get the ip address of these instances and perform other operations on them.


## 2. Deploy couchDB database cluster
This taks will execute ```db-deploy.yaml``` playbook whick consists of 6 roles. The instances used are load from ```inventory/inventory_file.ini```.
-   set-up-http-proxy
    - Adding HTTP_PROXY, HTTPS_PROXY, and NO_PROXY in ```/etc/environment``` directory on the instances so that the instance is able to access Internet and download dependencies.
- dependency
    - Install pip, vim, docker and other dependencies on the instances.
- set-up-docker-http-proxy
    - Set up docker HTTP_PROXY, HTTPS_PROXY, and NO_PROXY enviroment variables following the instruction from: https://docs.docker.com/config/daemon/systemd/#httphttps-proxy
    - Restart the docker and make sure new configuration has been loaded
- deploy-couchDB
    - Pull the couchDB image from and start docker container for couchDB
- deploy-couchDB-cluster
    - Set up the couchDB cluster by through the RESTful API, by default, the first node in the instance list is the master node of the cluster.
- deploy-couchDB-grunt
    - run “couch-compile” script, which processes the Couch Directory Tree
    - run“couch-push” script, which pushes the compiled documents to our couchdb database on MRC instances.

## 3. Deploy twitter harvester
This taks will execute ```harvester-deploy.yaml``` playbook whick consists of 6 roles. The instances used are load from ```inventory/inventory_file.ini```.
- deploy-twitter-harvester
    - Pull the twitter harvester image from docker hub and restart the container

## 4. Creating instances for webserver and data analyzer
This taks will execute ```webserver-create-instances.yaml``` palybook, similar to "Creating instances for database and harvesters", it will creare volumns, security group and the instace. However, it wil save the ip address in a different file
-   openstack-volume : 
-   openstack-security-group
-   openstack-instance
-   save-ip: 
    - The ip address will be automatically saved in ```inventory/inventory_webserver.ini```. The file can be used in subsequent tasks to get the ip address of these instances and perform other operations on them.
  
## 5. Deploy the webserver and data analyzer
This taks will execute ```webserver-deploy.yaml``` playbook whick consists of 5 roles. The instances used are load from ```inventory/inventory_webserver.ini```.
- set-up-http-proxy
- dependency
- set-up-docker-http-proxy
- deploy-data-analyzer
  - Pull the data analyzer image from the docker hub
  - attach ```/home/ubuntu/data``` directory on virtual machine at ```/code/data``` directory inside the container. This makesure the result of the data analyzer can be used by the web server.
- deploy-web-server
  - Pull the web server image form the docker hub
  - attach ```/home/ubuntu/data``` directory on virtual machine at ```/data``` directory inside the container. It will use the result produced by data analayer and show on the webpage.
 
