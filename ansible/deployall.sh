#!/bin/bash

echo "Creating instances for database and harvesters"
sh ./db-create-instances.sh

echo "Deploy couchDB database cluster"
sh ./db-deploy.sh

echo "Deploy twitter harvester"
sh ./harvester-deploy.sh

echo "Creating instances for database and harvesters"
sh ./webserver-create-instances.sh

echo "Deploy the webserver"
sh ./webserver.sh