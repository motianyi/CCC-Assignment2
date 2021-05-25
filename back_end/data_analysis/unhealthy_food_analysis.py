import data_loader as dl
import pandas as pd

def unhealthy_food_analyzer():
    tweets_melb_df = dl.df[dl.df['user_location'] == 'melbourne']
    tweets_syd_df = dl.df[dl.df['user_location'] == 'sydney']
    tweets_bris_df = dl.df[dl.df['user_location'] == 'brisbane']
    tweets_adel_df = dl.df[dl.df['user_location'] == 'adelaide']
    tweets_perth_df = dl.df[dl.df['user_location'] == 'perth']
    tweets_can_df = dl.df[dl.df['user_location'] == 'canberra']

    tweets_unhealthy_melb_df = dl.tweets_unhealthy_df[dl.tweets_unhealthy_df['user_location'] == 'melbourne']
    tweets_unhealthy_syd_df = dl.tweets_unhealthy_df[dl.tweets_unhealthy_df['user_location'] == 'sydney']
    tweets_unhealthy_bris_df = dl.tweets_unhealthy_df[dl.tweets_unhealthy_df['user_location'] == 'brisbane']
    tweets_unhealthy_adel_df = dl.tweets_unhealthy_df[dl.tweets_unhealthy_df['user_location'] == 'adelaide']
    tweets_unhealthy_perth_df = dl.tweets_unhealthy_df[dl.tweets_unhealthy_df['user_location'] == 'perth']
    tweets_unhealthy_can_df = dl.tweets_unhealthy_df[dl.tweets_unhealthy_df['user_location'] == 'canberra']

    unhealthy_food_info = pd.DataFrame(columns=['gcc_code16', 'gcc_name16', 'tweets_count', 'un/all in city','un/all un'])

    unhealthy_food_info.loc[0] = ['2GMEL','Greater Melbourne',len(tweets_unhealthy_melb_df),len(tweets_unhealthy_melb_df)/len(tweets_melb_df),len(tweets_unhealthy_melb_df)/len(dl.tweets_unhealthy_df)]
    unhealthy_food_info.loc[1] = ['1GSYD','Greater Sydney',len(tweets_unhealthy_syd_df),len(tweets_unhealthy_syd_df)/len(tweets_syd_df),len(tweets_unhealthy_syd_df)/len(dl.tweets_unhealthy_df)]
    unhealthy_food_info.loc[2] = ['3GBRI','Greater Brisbane',len(tweets_unhealthy_bris_df),len(tweets_unhealthy_bris_df)/len(tweets_bris_df),len(tweets_unhealthy_bris_df)/len(dl.tweets_unhealthy_df)]
    unhealthy_food_info.loc[3] = ['4GADE','Greater Adelaide',len(tweets_unhealthy_adel_df),len(tweets_unhealthy_adel_df)/len(tweets_adel_df),len(tweets_unhealthy_adel_df)/len(dl.tweets_unhealthy_df)]
    unhealthy_food_info.loc[4] = ['2GMEL','Greater Perth',len(tweets_unhealthy_perth_df),len(tweets_unhealthy_perth_df)/len(tweets_perth_df),len(tweets_unhealthy_perth_df)/len(dl.tweets_unhealthy_df)]
    unhealthy_food_info.loc[5] = ['8ACTE','Australian Capital Territory',len(tweets_unhealthy_can_df),len(tweets_unhealthy_can_df)/len(tweets_can_df),len(tweets_unhealthy_can_df)/len(dl.tweets_unhealthy_df)]
    unhealthy_food_info.loc[6] = ['nothing','Australia',len(dl.tweets_unhealthy_df),len(dl.tweets_unhealthy_df)/len(dl.df),len(dl.tweets_unhealthy_df)/len(dl.tweets_unhealthy_df)]

    print(unhealthy_food_info)


    unhealthy_food_json = unhealthy_food_info.T.to_json()
    fileObject = open('./data/{}'.format('unhealthy_food_analysis.json'), 'w')
    #fileObject = open('C:/Users/yanx5\Desktop/frontend_csv/{}'.format('unhealthy_food_analysis.json'), 'w')
    fileObject.write(unhealthy_food_json) 
    fileObject.close()   