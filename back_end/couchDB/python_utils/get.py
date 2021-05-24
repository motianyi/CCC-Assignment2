import util

ip_address = "172.26.133.138"
user_name = "admin"
password = "admin"
db_name = "covid_twitter"

design_doc_name = "hh_test1"
view_name = "new-view"
group_level = 13

result = util.get_view(ip_address,user_name,password,db_name,design_doc_name,view_name,group_level)
result2 = result["rows"]

i = 0
result_dic = {}
for item in result["rows"]:
    result_dic[i]=item["key"]
    i+=1
#print(result["rows"])
json_path = "./tweet_data.json"

util.write_json(json_path,result_dic)