import tweepy

  
# assign the values accordingly
consumer_key = '63HkbXgACUIyxLQB01fhC6oCu'  
consumer_secret = 'xeiCgyIbMCm37zAxy7sJhOuBXfYP8L0fUGqqx06BzBf3gUVLJI'  
access_token = '1065560839795617792-oZ8O8qELVKK7y8Q2FKF0gJej1gwCsv'  
access_token_secret = 'mGg4L5sEDyQ11GJ9WGeod8CYvlt5uhxJ6jrgWDqrG4dme'


class StreamListener(tweepy.StreamListener):

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

        
        print(text, tweet_location, user_location)

        
        with open("all_fifth.csv", "a", encoding='utf-8') as f:
            f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (text,
                                                               status.lang,
                                                               tweet_longitude,
                                                               tweet_latitude,
                                                               str(status.retweet_count),
                                                               str(status.favorite_count),
                                                               user_id,
                                                               user_location_first,
                                                               str(status.user.followers_count),
                                                               str(status.user.friends_count),
                                                               str(status.reply_count),
                                                               is_retweet,
                                                               is_quote,
                                                               status.created_at))
    

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