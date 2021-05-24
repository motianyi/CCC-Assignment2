import senti_analyzer as sa
import pandas as pd
import numpy as np
import csv

df = pd.read_csv("stream_and_search.csv",  low_memory=False)

tweets_income_df = df[df['text'].str.contains('income')]

df_income = pd.read_csv("income_search.csv",quoting=csv.QUOTE_NONE, encoding='utf-8')
col_list = ["text", "language", "longitude", "latitude", "retweet_count",
              "favorite_count", "user_id", "user_location", "followers_count",
              "friends_count",'is_retweet',"is_quote","tweet_created_at"]
df_income.columns = col_list

df_income = df_income.replace(np.nan,'nothing')
df_income['user_location'] = df_income['user_location'].str.lower()
df_income['text'] = df_income['text'].str.lower()
df_income = df_income.drop_duplicates()

df_income = pd.concat([df_income, tweets_income_df],ignore_index=True)

sa.sentiment_results_cal(df_income,'income_analysis.csv','income_analysis.json')

