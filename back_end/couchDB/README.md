# grunt_couchdb
grunt_couchdb is used to automatically deploy the couchdb database.

Use the following commands:
```bash
cd grunt_couchdb

npm install grunt-couch

grunt couch-compile

grunt couch-push
```
python_utils encapsulate the possilbe utils needed to interact with the database.
To get data from a sepicific view, run:
```
python get.py
```
The fetched data will be stored at ```python_utils/tweet_data.json```
