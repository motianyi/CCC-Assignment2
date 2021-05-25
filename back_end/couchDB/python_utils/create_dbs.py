import requests
import json

def create_db(ip_address,user_name,password,db_name):
    
    url = "http://{}:{}@{}:5984/{}".format(user_name,password,ip_address,db_name)
    print(url)
    response = requests.put(url)
    print(json.dumps(response.json()))

ip_address = "172.26.133.138"
user_name = "admin"
password = "admin"
db_name1 = "all_twitter"
db_name2 = "beer_twitter"
db_name3 = "covid_twitter"
db_name4 = "income_twitter"

create_db(ip_address,user_name,password,db_name1)
create_db(ip_address,user_name,password,db_name2)
create_db(ip_address,user_name,password,db_name3)
create_db(ip_address,user_name,password,db_name4)

