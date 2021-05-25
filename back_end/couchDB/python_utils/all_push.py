import requests
import json

def insert_json(ip_address,user_name,password,db_name,json_path):
    url = "http://{}:{}@{}:5984/{}".format(user_name,password,ip_address,db_name)
    header = {"Content-Type": "application/json"}

    with open(json_path,"r") as f:
        #data = json.dumps(json.load(f))
        temp_data = json.load(f)

    #load item one by one
    for item in temp_data["docs"]:
        response = requests.post(
            url,
            headers = header,
            data = json.dumps(item)
        )
        print(json.dumps(response.json()))

ip_address = "172.26.133.138"
user_name = "admin"
password = "admin"
db_name = "all_twitter"
###json_path need to change
json_path = "./all_data.json"

insert_json(ip_address,user_name,password,db_name,json_path)
