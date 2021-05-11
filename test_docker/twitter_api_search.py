import tweepy
import twitter_utils
import couchdb_utils  
import json

# assign the values accordingly
consumer_key = 'Sc7HCaqRZp8igs8NG2rpxyHu9'  
consumer_secret = 'cZXAcseeOHkm05CnL52ThwL6s1DnBFaqTaHIYqLJefS4PiXEE6'  
access_token = '1065560839795617792-TYvHaQzQbJ4BP23zCvlXwcyA3NQbnK'  
access_token_secret = 'xZZeqDYUiqduhK1Hr0bm4cVnKu0QrhF4QFucHB1b0KFpR'

#get api access
twitter_api = twitter_utils.get_apiaccess(consumer_key,consumer_secret,access_token,access_token_secret)

#set search rules
key_word_list = ['cat','dog','bird']
geocode_value = "-37.840935,144.946457,10km"
tweet_num = 10

#get tweet based on rules
result = twitter_utils.get_tweet(key_word_list, geocode_value,tweet_num,twitter_api)

#write result to json file
list_for_write = []
for item in result:
   for tweet in item:
      list_for_write.append({"tweet_id":tweet.id,"tweet_text":tweet.text,"tweet_location":tweet.user.location})

json_file={"docs":list_for_write}
file_path = "./tweetapi_search_data.json"
twitter_utils.write_json(file_path, json_file)

# send json file to couchdb
ip_address = "172.26.134.17"
user_name = "admin"
password = "admin"
db_name = "test_db"
json_path = "./tweetapi_search_data.json"
couchdb_utils.insert_json(ip_address,user_name,password,db_name,json_path)