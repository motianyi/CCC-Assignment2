import tweepy
import utils  
import json
# assign the values accordingly
consumer_key = 'Sc7HCaqRZp8igs8NG2rpxyHu9'  
consumer_secret = 'cZXAcseeOHkm05CnL52ThwL6s1DnBFaqTaHIYqLJefS4PiXEE6'  
access_token = '1065560839795617792-TYvHaQzQbJ4BP23zCvlXwcyA3NQbnK'  
access_token_secret = 'xZZeqDYUiqduhK1Hr0bm4cVnKu0QrhF4QFucHB1b0KFpR'
  
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth)
  
#cricTweet = tweepy.Cursor(api.search, q='cricket', geocode="-37.840935,144.946457,10km").items(100)

def get_tweet(key_word_list,geocode_value,tweet_num):
   result_list = []
   for item in key_word_list:
      cricTweets = tweepy.Cursor(api.search, q=item, geocode=geocode_value).items(tweet_num)
      result_list.append(cricTweets)

   return(result_list)

key_word_list = ['cat','dog','bird']
geocode_value = "-37.840935,144.946457,10km"
tweet_num = 10
result = get_tweet(key_word_list, geocode_value,tweet_num)

list_for_write = []
for item in result:
   for tweet in item:
      list_for_write.append({"tweet_id":tweet.id,"tweet_text":tweet.text,"tweet_location":tweet.user.location})

json_file={"docs":list_for_write}
file_path = "./tweet_data.json"
utils.write_json(file_path, json_file)
   #print(item.text)
#for tweet in cricTweet:
   #print(tweet.created_at, tweet.text, tweet.lang)
   #print(tweet.text,tweet.user.location)
