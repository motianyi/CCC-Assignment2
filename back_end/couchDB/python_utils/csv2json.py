import pandas as pd 
import util
all_tweets = pd.read_csv("./twitter_data/all.csv")
column_name = ['text','lang','tweet_longitude','tweet_latitude','retweet_count','favorite_count','user_id','user_location_first','user_followers_count','user_friends_count','is_retweet','is_quote','created_at']
all_tweets.columns = column_name
test = all_tweets.T.to_dict()

doc_list = []
for key in test:
    doc_list.append(test[key])

json_dic = {"docs":doc_list}
util.write_json("./data.json",json_dic)