import pandas as pd
import requests

ip_address = "172.26.133.138"
user_name = "admin"
password = "admin"
income_db_name = "income_twitter"
beer_db_name = "beer_twitter"
all_db_name = "all_twitter"
covid_db_name = "covid_twitter"

design_doc_name = "twitter_view1"
view_name = "all_remove_duplicate"
group_level = 13


def get_view(ip_address,user_name,password,db_name,design_doc_name,view_name,group_level):
    url = "http://{}:{}@{}:5984/{}/_design/{}/_view/{}?reduce=true&group_level={}".format(user_name,password,ip_address,db_name,design_doc_name,view_name,group_level)
    #print(url)
    response = requests.get(url)
    result = response.json()
    #result = json.dumps(response.json())
    #print(result)
    return result

def get_income_twitter():
    result = get_view(ip_address,user_name,password,income_db_name,design_doc_name,view_name,group_level)

    i = 0
    result_dic = {}
    for item in result["rows"]:
        result_dic[i]=item["key"]
        i+=1

    data = pd.DataFrame(result_dic).T
    data.columns = ['text','language','longitude','latitude','retweet_count','favorite_count','user_id','user_location','followers_count','friends_count','is_retweet','is_quote','tweet_created_at']

    return data


def get_beer_twitter():
    result = get_view(ip_address,user_name,password,beer_db_name,design_doc_name,view_name,group_level)

    i = 0
    result_dic = {}
    for item in result["rows"]:
        result_dic[i]=item["key"]
        i+=1

    data = pd.DataFrame(result_dic).T
    data.columns = ['text','language','longitude','latitude','retweet_count','favorite_count','user_id','user_location','followers_count','friends_count','is_retweet','is_quote','tweet_created_at']

    return data

def get_covid_twitter():
    result = get_view(ip_address,user_name,password,covid_db_name,design_doc_name,view_name,group_level)

    i = 0
    result_dic = {}
    for item in result["rows"]:
        result_dic[i]=item["key"]
        i+=1

    data = pd.DataFrame(result_dic).T
    data.columns = ['text','language','longitude','latitude','retweet_count','favorite_count','user_id','user_location','followers_count','friends_count','is_retweet','is_quote','tweet_created_at']

    return data


def get_all_twitter():
    result = get_view(ip_address,user_name,password,all_db_name,design_doc_name,view_name,group_level)

    i = 0
    result_dic = {}
    for item in result["rows"]:
        result_dic[i]=item["key"]
        i+=1

    data = pd.DataFrame(result_dic).T
    data.columns = ['text','language','longitude','latitude','retweet_count','favorite_count','user_id','user_location','followers_count','friends_count','is_retweet','is_quote','tweet_created_at']

    return data

#print(get_beer_twitter())

#json_path = "./income_tweet_data.json"

#util.write_json(json_path,result_dic)