import util


ip_address = "172.26.133.138"
user_name = "admin"
password = "admin"
db_name = "twitter"

design_doc_name = "test_design"
view_name = "city"
group_level = 1

result = util.get_view(ip_address,user_name,password,db_name,design_doc_name,view_name,group_level)

json_path = "./tweet_data.json"

util.write_json(json_path,result)