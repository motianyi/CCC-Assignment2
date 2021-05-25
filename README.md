# CCC-Assignment2
## Ansible
We used ansible to automatically do the following tasks:
  - Setting up security group rules in the project
  - Managing the volumes and instances creation on the Melbourne Research Clouds
  - Installing dependencies and tools on the instances
  - Setting up and launching the CouchDB cluster.
  - Launching the Data Harvester.
  - Launching the Data Analyzer.
  - Launching the Web Server.

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
