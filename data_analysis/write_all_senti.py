import senti_analyzer as sa
import pandas as pd
import numpy as np
import csv

df = pd.read_csv("stream_and_search.csv",  low_memory=False)
sa.sentiment_results_cal(df,'all_senti_analysis.csv','all_senti_analysis.json')


# has geo tweets


tweets_geo_df = df[df['longitude'] != 'nothing']
sa.sentiment_results_cal(tweets_geo_df,'has_geo_senti_analysis.csv','has_geo_senti_analysis.json')


# has covid or corona tweets

tweets_covid_df = df[df['text'].str.contains('covid')]
tweets_corona_df = df[df['text'].str.contains('coronavirus')]

tweets_covid_all_df = pd.concat([tweets_covid_df, tweets_corona_df],ignore_index=True)
texts_covid_all_df = tweets_covid_all_df['text']

df_covid = pd.read_csv("covid_search.csv",quoting=csv.QUOTE_NONE, encoding='utf-8')
col_list_covid = ["text", "language", "longitude", "latitude", "retweet_count",
              "favorite_count", "user_id", "user_location", "followers_count",
              "friends_count",'is_retweet',"is_quote","tweet_created_at"]
df_covid.columns = col_list_covid

df_covid = df_covid.replace(np.nan,'nothing')
df_covid['user_location'] = df_covid['user_location'].str.lower()
df_covid['text'] = df_covid['text'].str.lower()
df_covid = df_covid.drop_duplicates()
df_covid = pd.concat([df_covid, tweets_covid_all_df],ignore_index=True)

sa.sentiment_results_cal(df_covid,'covid_senti_analysis.csv','covid_senti_analysis.json')

