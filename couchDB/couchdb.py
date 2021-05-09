import util

ip_address = "172.26.134.17"
user_name = "admin"
password = "admin"
db_name = "test_db"
###json_path need to change
json_path = "./tweet_data.json"
###view_path need to change
design_doc_path = "./view.json"
design_doc_name = "counter2"
view_name = "count"
group_level = 1
#util.get_db_list(ip_address,user_name,password)
#util.create_db(ip_address,user_name,password,db_name)
#util.insert_json(ip_address,user_name,password,db_name,json_path)
#util.add_view(ip_address,user_name,password,db_name,design_doc_name,design_doc_path)
result = util.get_view(ip_address,user_name,password,db_name,design_doc_name,view_name,group_level)
print(type(result))
print(result)