import requests
import json

def create_db(ip_address,user_name,password,db_name):
    
    url = "http://{}:{}@{}:5984/{}".format(user_name,password,ip_address,db_name)
    print(url)
    response = requests.put(url)
    print(json.dumps(response.json()))

def get_db_list(ip_address,user_name,password):
    url = "http://{}:{}@{}:5984/{}".format(user_name,password,ip_address,"_all_dbs")
    response = requests.get(url)
    result = json.dumps(response.json())
    print(result)
    return result

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
    '''
    response = requests.post(
        url,
        headers = header,
        params = data
    )
    print(json.dumps(response.json()))
    '''
    
def add_view(ip_address,user_name,password,db_name,design_doc_name,design_doc_path):#view is a mapreduce json file
    url = "http://{}:{}@{}:5984/{}/_design/{}".format(user_name,password,ip_address,db_name,design_doc_name)
    header = {"Content-Type": "application/json"}
    with open(design_doc_path,"r") as f:
        data = json.dumps(json.load(f))
    
    response = requests.put(
        url,
        headers = header,
        data = data
    )

    print(json.dumps(response.json()))

def get_view(ip_address,user_name,password,db_name,design_doc_name,view_name,group_level):
    url = "http://{}:{}@{}:5984/{}/_design/{}/_view/{}?reduce=true&group_level={}".format(user_name,password,ip_address,db_name,design_doc_name,view_name,group_level)
    #print(url)
    response = requests.get(url)
    result = response.json()
    #result = json.dumps(response.json())
    #print(result)
    return result
    
def write_json(file_path,content):
    with open(file_path,"w") as f:
        json.dump(content,f)
        print("write json successfully")

def load_json(file_path):
    with open(file_path,"r") as f:
        result = json.load(f)
        print("load json successfully")
    return result




