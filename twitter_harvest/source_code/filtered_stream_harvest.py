import utils

bearer_token = "AAAAAAAAAAAAAAAAAAAAABHZOgEAAAAAd6vgSgWd%2BXJyUtXbbK%2BSo97nx9o%3D4tBPb5WuwUPGFKRTqL2Psh8LmORuC28o9h5ATRXPmA64vrjltJ"
header_value = utils.authorization(bearer_token)

#sample of rules
#sample:15 in line 9 means randomly select 15% of the total tweets
rules = [
    {"value": "dog has:images sample:15", "tag": "dog pictures"},
    {"value": "cat has:images -grumpy", "tag": "cat pictures"}
]

#sample of rules ids
rule_id_list = [
    "1390595466019020807",
    "1390653720405237761"
]

#utils.delete_rules(header_value, rule_id_list)
#utils.add_rules(header_value, rules)
#utils.get_rules(header_value)
result = utils.get_stream_limited(header_value, 5)
#utils.get_stream(header_value)

file_path = "./tweet_data"

#write json file
json_dic = {}
for i in range(0,len(result)):
    temp_index = "tweet {}".format(i)
    json_dic[temp_index] = result[i]

utils.write_json(file_path, json_dic)
