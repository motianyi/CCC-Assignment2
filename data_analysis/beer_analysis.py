import pandas as pd

df = pd.read_csv("stream_and_search.csv",  low_memory=False)

beer_df = pd.read_csv("beer_search.csv")
col_list = ["text", "language", "longitude", "latitude", "retweet_count",
              "favorite_count", "user_id", "user_location", "followers_count",
              "friends_count",'is_retweet',"is_quote","tweet_created_at"]
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


beer_in_all_df = df[df['text'].str.contains('beer')]


tweets_melb_df = df[df['user_location'] == 'melbourne']
tweets_syd_df = df[df['user_location'] == 'sydney']
tweets_bris_df = df[df['user_location'] == 'brisbane']
tweets_adel_df = df[df['user_location'] == 'adelaide']
tweets_perth_df = df[df['user_location'] == 'perth']
tweets_can_df = df[df['user_location'] == 'canberra']

beer_melb_df = beer_df[beer_df['user_location'] == 'melbourne']
beer_syd_df = beer_df[beer_df['user_location'] == 'sydney']
beer_bris_df = beer_df[beer_df['user_location'] == 'brisbane']
beer_adel_df = beer_df[beer_df['user_location'] == 'adelaide']
beer_perth_df = beer_df[beer_df['user_location'] == 'perth']
beer_can_df = beer_df[beer_df['user_location'] == 'canberra']

beer_in_all_melb_df = beer_in_all_df[beer_in_all_df['user_location'] == 'melbourne']
beer_in_all_syd_df = beer_in_all_df[beer_in_all_df['user_location'] == 'sydney']
beer_in_all_bris_df = beer_in_all_df[beer_in_all_df['user_location'] == 'brisbane']
beer_in_all_adel_df = beer_in_all_df[beer_in_all_df['user_location'] == 'adelaide']
beer_in_all_perth_df = beer_in_all_df[beer_in_all_df['user_location'] == 'perth']
beer_in_all_can_df = beer_in_all_df[beer_in_all_df['user_location'] == 'canberra']

beer_info = pd.DataFrame(columns=['gcc_code16', 'gcc_name16', 'tweets_count', 'beer/all in city', 'beer/all beer'])

beer_info.loc[0] = ['2GMEL','Greater Melbourne',len(beer_melb_df),len(beer_in_all_melb_df)/len(tweets_melb_df),len(beer_melb_df)/len(beer_df)]
beer_info.loc[1] = ['1GSYD','Greater Sydney',len(beer_syd_df),len(beer_in_all_syd_df)/len(tweets_syd_df),len(beer_syd_df)/len(beer_df)]
beer_info.loc[2] = ['3GBRI','Greater Brisbane',len(beer_bris_df),len(beer_in_all_bris_df)/len(tweets_bris_df),len(beer_bris_df)/len(beer_df)]
beer_info.loc[3] = ['4GADE','Greater Adelaide',len(beer_adel_df),len(beer_in_all_adel_df)/len(tweets_adel_df),len(beer_adel_df)/len(beer_df)]
beer_info.loc[4] = ['2GMEL','Greater Perth',len(beer_perth_df),len(beer_in_all_perth_df)/len(tweets_perth_df),len(beer_perth_df)/len(beer_df)]
beer_info.loc[5] = ['8ACTE','Australian Capital Territory',len(beer_can_df),len(beer_in_all_can_df)/len(tweets_can_df),len(beer_can_df)/len(beer_df)]
beer_info.loc[6] = ['nothing','Australia',len(beer_df),len(beer_in_all_df)/len(df),len(beer_df)/len(beer_df)]

print(beer_info)

beer_info.to_csv (r'C:/Users/yanx5\Desktop/frontend_csv/{}'.format('beer_analysis.csv'), index = False, header=True)

unhealthy_food_json = beer_info.T.to_json()
fileObject = open('C:/Users/yanx5\Desktop/frontend_csv/{}'.format('beer_analysis.json'), 'w')
fileObject.write(unhealthy_food_json) 
fileObject.close()