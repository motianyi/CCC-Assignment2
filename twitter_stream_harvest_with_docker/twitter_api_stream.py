import tweepy
import json
import requests
  
# assign the values accordingly
consumer_key = 'oJ9ONNts9643YrJUPTfruyddN'  
consumer_secret = 'iKSV8bFRIN0Ygqw6w0cYmTVHY5sDpvHlRLyHkvVwr0XijH6lIQ'  
access_token = '1384022067817766914-V1vvbKj34e2ZsT2qsdzIMzCoCmx0mu'  
access_token_secret = 'w0FWHEeLQ3wylHHftbSt4E6Cqo7Y9zCIg32lGSjfqcmiq'


class StreamListener(tweepy.StreamListener):

    def write_json(file_path,content):
        with open(file_path,"w") as f:
            json.dump(content,f)
        print("write json successfully")

    def on_status(self, status):
        is_retweet = hasattr(status, "retweeted_status")
        is_quote = hasattr(status, "quoted_status")
        text = status.text
        user_location = status.user.location
        tweet_location = status.coordinates
        user_id = status.user.id_str
        
                
        remove_characters = [",","\n"]
        for c in remove_characters:
            text = text.replace(c," ")
        http_index = text.find('http')
        text = text[0:http_index]


        if user_location == None:
            user_location_first = "N/A"
        else:
            user_location_list = user_location.split(",")
            user_location_first = user_location_list[0]


        if tweet_location == None:
            tweet_longitude = "N/A"
            tweet_latitude = "N/A"
        else:
            tweet_longitude = str(tweet_location['coordinates'][0])
            tweet_latitude = str(tweet_location['coordinates'][1])

        
        #print(text, tweet_location, user_location)

        temp_dic = {
            "text":text,
            "lang":status.lang,
            "tweet_longitude":tweet_longitude,
            "tweet_latitude":tweet_latitude,
            "retweet_count":str(status.retweet_count),
            "favorite_count":str(status.favorite_count),
            "user_id":user_id,
            "user_location_first":user_location_first,
            "user_followers_count":str(status.user.followers_count),
            "user_friends_count":str(status.user.friends_count),
            "reply_count":str(status.reply_count),
            "is_retweet":is_retweet,
            "is_quote":is_quote,
            "created_at":str(status.created_at)
        }
        result = json.dumps(temp_dic)



        ip_address = "172.26.128.223"
        user_name = "admin"
        password = "admin"
        db_name = "twitter"
        url = "http://{}:{}@{}:5984/{}".format(user_name,password,ip_address,db_name)
        
        response = requests.post(
            url,
            headers = {"Content-Type": "application/json"},
            data = json.dumps(temp_dic)
            )
        print(json.dumps(response.json()))
    

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")


if __name__ == "__main__":

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)


    streamListener = StreamListener()
    #stream = tweepy.Stream(auth=api.auth, listener=streamListener, tweet_mode='extended')
    stream = tweepy.Stream(auth=api.auth, listener=streamListener)


    australia_bounding = (113.338953078, -43.6345972634, 153.569469029, -10.6681857235)
    #tags = [' ']
    #kpop_tags = [' ']
    covid_tags = ['covid','coronavirus','lockdown']
    #stream.filter(locations=australia_bounding,track=covid_tags)
    stream.filter(locations=australia_bounding)