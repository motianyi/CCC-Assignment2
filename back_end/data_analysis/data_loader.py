import pandas as pd
import csv
import numpy as np
import get

col_list = ["text", "language", "longitude", "latitude", "retweet_count",
              "favorite_count", "user_id", "user_location", "followers_count",
              "friends_count",'is_retweet',"is_quote","tweet_created_at"]
unhealthy_food_list = ['coke','cola','pepsi','7up','chips','fried chicken','popcorn','cream','pizza','fast food','fastfood','pancake','burger','milkshake','doughnut','hotdog','hot dog','cupcake','sweets','candy','french fries']
unhealthy_restaurant_list = ['kfc','hungry jack', "nando's", "nandos", 'mcdonald', 'oporto', 'red rooster', 'guzman y gomez', 'guzman']

# all_df
#df = pd.read_csv("stream_and_search.csv",  low_memory=False)
df = get.get_all_twitter()
df.columns = col_list


# has_geo_df
tweets_geo_df = df[df['longitude'] != 'nothing']

# covid_df
tweets_covid_df = df[df['text'].str.contains('covid')]
tweets_corona_df = df[df['text'].str.contains('coronavirus')]
tweets_covid_in_all_df = pd.concat([tweets_covid_df, tweets_corona_df],ignore_index=True)

#df_covid = pd.read_csv("covid_search.csv",quoting=csv.QUOTE_NONE, encoding='utf-8')
df_covid = get.get_covid_twitter()
col_list = ["text", "language", "longitude", "latitude", "retweet_count",
              "favorite_count", "user_id", "user_location", "followers_count",
              "friends_count",'is_retweet',"is_quote","tweet_created_at"]
df_covid.columns = col_list

df_covid = df_covid.replace(np.nan,'nothing')
df_covid['user_location'] = df_covid['user_location'].str.lower()
df_covid['text'] = df_covid['text'].str.lower()
df_covid = df_covid.drop_duplicates()
df_covid = pd.concat([df_covid, tweets_covid_in_all_df],ignore_index=True)

# covid_vaccine_df
tweets_covid_vaccine_df = df_covid[df_covid['text'].str.contains('vaccine')]

# unhealthy_food_df
tweets_unhealthy_df = df[df['text'].str.contains('donut')]
for food in unhealthy_food_list + unhealthy_restaurant_list:
    current_df = df[df['text'].str.contains(food)]
    tweets_unhealthy_df = pd.concat([tweets_unhealthy_df, current_df],ignore_index=True)

# beer_df
tweets_beer_in_all_df = df[df['text'].str.contains('beer')]


beer_df = get.get_beer_twitter()
#beer_df = pd.read_csv("beer_search.csv")
beer_df.columns = col_list
beer_df['user_location'] = beer_df['user_location'].str.lower()
beer_df['text'] = beer_df['text'].str.lower()
c_drop = 0
drop_indexs = []
len_l = []
for i in range(len(beer_df)):
    if len(str(beer_df['text'][i]).split(' ')) > 100:
        drop_indexs.append(i)
        len_l.append(len(str(beer_df['text'][i]).split(' ')))
        c_drop += 1

drop_or_not = []
for i in range(len(beer_df)):
    if i not in drop_indexs:
        drop_or_not.append(True)
    else:
        drop_or_not.append(False)

beer_df = beer_df[drop_or_not]
beer_df = beer_df.drop_duplicates()

beer_df = pd.concat([beer_df, tweets_beer_in_all_df],ignore_index=True)

# income_df
tweets_income_in_all_df = df[df['text'].str.contains('income')]

df_income = get.get_income_twitter()
#df_income = pd.read_csv("income_search.csv",quoting=csv.QUOTE_NONE, encoding='utf-8')
df_income.columns = col_list

df_income = df_income.replace(np.nan,'nothing')
df_income['user_location'] = df_income['user_location'].str.lower()
df_income['text'] = df_income['text'].str.lower()
df_income = df_income.drop_duplicates()

df_income = pd.concat([df_income, tweets_income_in_all_df],ignore_index=True)