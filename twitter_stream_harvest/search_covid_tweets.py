import tweepy
import time
  
# assign the values accordingly
consumer_key = '7JJmR6WKltv8A1me6OC59bWJB'  
consumer_secret = 'u5oFOgaFJrwLqeO6yx9RYLK204xTeCutPSYCbP2pi7VBk1Wezy'  
access_token = '1252574059885236225-Ey0mZB9xIm4UKhQCrCUcstxtkAU1V3'  
access_token_secret = 'ryrZHx48KCC2d2MHmrZlw6Zmg10oZDkL9nC6GhcUctKfj'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKp8PwEAAAAA4CcQXxDgeuiMcZm3%2BdpHa5tP%2FTs%3DfJogwgGmpkl0e8wPLPQ7TK7B32IAuoouA6VSJLISKOFCWtTWmi'

def search_write_covid():
   # authorization of consumer key and consumer secret
   auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
   
   # set access to user's access key and access secret 
   auth.set_access_token(access_token, access_token_secret)
   
   # calling the api 
   api = tweepy.API(auth)
   
   covid_tweet = tweepy.Cursor(api.search, q = 'covid' or 'coronavirus',  geocode ="-24.25,133.416667,2100km").items(2400)
   #covid_tweet = tweepy.Cursor(api.search, q = 'kpop',  geocode ="-24.25,133.416667,2100km").items(2400)

   for tweet in covid_tweet:
      #print(tweet.created_at, tweet.text, tweet.lang)
      print(tweet.text)
      
      is_retweet = hasattr(tweet, "retweeted_status")
      is_quote = hasattr(tweet, "quoted_status")
      text = tweet.text
      user_location = tweet.user.location
      tweet_location = tweet.coordinates
      user_id = tweet.user.id_str


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

         
      with open("covid_search.csv", "a", encoding='utf-8') as f:
         f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (text,
                                                               tweet.lang,
                                                               tweet_longitude,
                                                               tweet_latitude,
                                                               str(tweet.retweet_count),
                                                               str(tweet.favorite_count),
                                                               user_id,
                                                               user_location_first,
                                                               str(tweet.user.followers_count),
                                                               str(tweet.user.friends_count),
                                                                  #str(tweet.reply_count),
                                                               is_retweet,
                                                               is_quote,
                                                               tweet.created_at))

def loop_search_covid():
   while True:
      search_write_covid()
      time.sleep(43200)


if __name__ == "__main__":
   loop_search_covid()