import tweepy
import pandas as pd
import csv
# assign the values accordingly
consumer_key = '7JJmR6WKltv8A1me6OC59bWJB'  
consumer_secret = 'u5oFOgaFJrwLqeO6yx9RYLK204xTeCutPSYCbP2pi7VBk1Wezy'  
access_token = '1252574059885236225-Ey0mZB9xIm4UKhQCrCUcstxtkAU1V3'  
access_token_secret = 'ryrZHx48KCC2d2MHmrZlw6Zmg10oZDkL9nC6GhcUctKfj'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKp8PwEAAAAA4CcQXxDgeuiMcZm3%2BdpHa5tP%2FTs%3DfJogwgGmpkl0e8wPLPQ7TK7B32IAuoouA6VSJLISKOFCWtTWmi'

df = pd.read_csv("has_geo_df.csv", quoting=csv.QUOTE_NONE, encoding='utf-8', low_memory=False)
user_ids = df['user_id']
user_ids.drop_duplicates()
#print(user_ids[:1000])

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

count = 0
#for user_id in user_ids[1000:3000]:
for user_id in user_ids:
    try:
        id = int(user_id)
        statuses = api.user_timeline(id)
        print(count)
    except tweepy.error.TweepError:
        print(count)
        print("Not authoorized")
    else:
        for status in statuses:
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

            
            with open("has_geo_user_timeline_search.csv", "a", encoding='utf-8') as f:
                f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (text,
                                                                status.lang,
                                                                tweet_longitude,
                                                                tweet_latitude,
                                                                str(status.retweet_count),
                                                                str(status.favorite_count),
                                                                user_id,
                                                                user_location_first,
                                                                str(status.user.followers_count),
                                                                str(status.user.friends_count),
                                                                #str(status.reply_count),
                                                                is_retweet,
                                                                is_quote,
                                                                status.created_at))
    count += 1