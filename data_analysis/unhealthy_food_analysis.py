import pandas as pd

unhealthy_food_list = ['coke','cola','pepsi','7up','chips','fried chicken','popcorn','cream','pizza','fast food','fastfood','pancake','burger','milkshake','doughnut','hotdog','hot dog','cupcake','sweets','candy','french fries']
unhealthy_restaurant_list = ['kfc','hungry jack', "nando's", "nandos", 'mcdonald', 'oporto', 'red rooster', 'guzman y gomez', 'guzman']

df = pd.read_csv("stream_and_search.csv",  low_memory=False)

tweets_unhealthy_df = df[df['text'].str.contains('donut')]

for food in unhealthy_food_list + unhealthy_restaurant_list:
    current_df = df[df['text'].str.contains(food)]
    tweets_unhealthy_df = pd.concat([tweets_unhealthy_df, current_df],ignore_index=True)

tweets_melb_df = df[df['user_location'] == 'melbourne']
tweets_syd_df = df[df['user_location'] == 'sydney']
tweets_bris_df = df[df['user_location'] == 'brisbane']
tweets_adel_df = df[df['user_location'] == 'adelaide']
tweets_perth_df = df[df['user_location'] == 'perth']
tweets_can_df = df[df['user_location'] == 'canberra']

tweets_unhealthy_melb_df = tweets_unhealthy_df[tweets_unhealthy_df['user_location'] == 'melbourne']
tweets_unhealthy_syd_df = tweets_unhealthy_df[tweets_unhealthy_df['user_location'] == 'sydney']
tweets_unhealthy_bris_df = tweets_unhealthy_df[tweets_unhealthy_df['user_location'] == 'brisbane']
tweets_unhealthy_adel_df = tweets_unhealthy_df[tweets_unhealthy_df['user_location'] == 'adelaide']
tweets_unhealthy_perth_df = tweets_unhealthy_df[tweets_unhealthy_df['user_location'] == 'perth']
tweets_unhealthy_can_df = tweets_unhealthy_df[tweets_unhealthy_df['user_location'] == 'canberra']

unhealthy_food_info = pd.DataFrame(columns=['gcc_code16', 'gcc_name16', 'tweets_count', 'percentage'])

unhealthy_food_info.loc[0] = ['2GMEL','Greater Melbourne',len(tweets_unhealthy_melb_df),len(tweets_unhealthy_melb_df)/len(tweets_melb_df)]
unhealthy_food_info.loc[1] = ['1GSYD','Greater Sydney',len(tweets_unhealthy_syd_df),len(tweets_unhealthy_syd_df)/len(tweets_syd_df)]
unhealthy_food_info.loc[2] = ['3GBRI','Greater Brisbane',len(tweets_unhealthy_bris_df),len(tweets_unhealthy_bris_df)/len(tweets_bris_df)]
unhealthy_food_info.loc[3] = ['4GADE','Greater Adelaide',len(tweets_unhealthy_adel_df),len(tweets_unhealthy_adel_df)/len(tweets_adel_df)]
unhealthy_food_info.loc[4] = ['2GMEL','Greater Perth',len(tweets_unhealthy_perth_df),len(tweets_unhealthy_perth_df)/len(tweets_perth_df)]
unhealthy_food_info.loc[5] = ['8ACTE','Australian Capital Territory',len(tweets_unhealthy_can_df),len(tweets_unhealthy_can_df)/len(tweets_can_df)]
unhealthy_food_info.loc[6] = ['nothing','Australia',len(tweets_unhealthy_df),len(tweets_unhealthy_df)/len(df)]

print(unhealthy_food_info)

unhealthy_food_info.to_csv (r'C:/Users/yanx5\Desktop/frontend_csv/{}'.format('unhealthy_food_analysis.csv'), index = False, header=True)

unhealthy_food_json = unhealthy_food_info.T.to_json()
fileObject = open('C:/Users/yanx5\Desktop/frontend_csv/{}'.format('unhealthy_food_analysis.json'), 'w')
fileObject.write(unhealthy_food_json) 
fileObject.close()