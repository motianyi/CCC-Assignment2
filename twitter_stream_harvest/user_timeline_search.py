import tweepy
import pandas as pd
import csv
import time
# assign the values accordingly
consumer_key = 'j3b3PWq7LnrUa1vNGHBPc2Q51'  
consumer_secret = 'oXO0zpl90FO723ClkNS0v1XQYyoVb3uyeg9BAbU0RBR30jnNri'  
access_token = '1065560839795617792-CJAjycsjB15Lugx1SBWeRuVlNIGZKS'  
access_token_secret = 'dYYPuvIPHcA65nRjB1HNyccGM78wGtLlhgk1CwOLnpLbM'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAFKrPwEAAAAAMpo30edi100KWbYjN2Lywu16BGU%3DNezyDTwSv2NUlsFYJW7xdpuxJyNQ5sV2taFgICFiZGvQm0VQDU'

df = pd.read_csv("all.csv", quoting=csv.QUOTE_NONE, encoding='utf-8', low_memory=False)
user_ids = df['user_id']
user_ids.drop_duplicates()
#print(user_ids[:1000])

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

count = 0
count_error = 0
for i in range (len(user_ids)):
    try:
        id = int(user_ids[i])
        statuses = api.user_timeline(id)
        print(count)
    except tweepy.error.TweepError:
        print(count)
        print("Not authoorized")
        count_error += 1
        if count_error >= 10:
            count_error = count_error -10
            i = i - 10
            count = count - 10
            time.sleep(900)
    else:
        count_error = 0
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

            
            with open("user_timeline_search_yan.csv", "a", encoding='utf-8') as f:
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
