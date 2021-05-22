# Deployment using Ansible

The whole sysetem consists of webserver, couchdb database and data harvester. In order to deploy the whole system on the Melbouren Research Cloud (MRC). 
If you want to create and deploy all parts of the system, you can execute the following command from the ```ansible``` directory. 
```bash
sh ./deployall.sh
```
The following showed the command will run in ```deployall.sh```. In some occasions, for example if the instance is already created, you can run commands to do spcific tasks.
```bash
#!/bin/bash

# Creating instances for database and harvesters
sh ./db-create-instances.sh

# echo "Deploy couchDB database cluster
sh ./db-deploy.sh

# echo "Deploy twitter harvester
sh ./harvester-deploy.sh

# Creating instances for database and harvesters
sh ./webserver-create-instances.sh

# echo "Deploy the webserver
sh ./webserver-deploy.sh
```
