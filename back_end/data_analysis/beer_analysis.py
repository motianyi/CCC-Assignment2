import data_loader as dl
import pandas as pd
def beer_analyzer():
    tweets_melb_df = dl.df[dl.df['user_location'] == 'melbourne']
    tweets_syd_df = dl.df[dl.df['user_location'] == 'sydney']
    tweets_bris_df = dl.df[dl.df['user_location'] == 'brisbane']
    tweets_adel_df = dl.df[dl.df['user_location'] == 'adelaide']
    tweets_perth_df = dl.df[dl.df['user_location'] == 'perth']
    tweets_can_df = dl.df[dl.df['user_location'] == 'canberra']

    beer_melb_df = dl.beer_df[dl.beer_df['user_location'] == 'melbourne']
    beer_syd_df = dl.beer_df[dl.beer_df['user_location'] == 'sydney']
    beer_bris_df = dl.beer_df[dl.beer_df['user_location'] == 'brisbane']
    beer_adel_df = dl.beer_df[dl.beer_df['user_location'] == 'adelaide']
    beer_perth_df = dl.beer_df[dl.beer_df['user_location'] == 'perth']
    beer_can_df = dl.beer_df[dl.beer_df['user_location'] == 'canberra']

    beer_in_all_melb_df = dl.tweets_beer_in_all_df[dl.tweets_beer_in_all_df['user_location'] == 'melbourne']
    beer_in_all_syd_df = dl.tweets_beer_in_all_df[dl.tweets_beer_in_all_df['user_location'] == 'sydney']
    beer_in_all_bris_df = dl.tweets_beer_in_all_df[dl.tweets_beer_in_all_df['user_location'] == 'brisbane']
    beer_in_all_adel_df = dl.tweets_beer_in_all_df[dl.tweets_beer_in_all_df['user_location'] == 'adelaide']
    beer_in_all_perth_df = dl.tweets_beer_in_all_df[dl.tweets_beer_in_all_df['user_location'] == 'perth']        
    beer_in_all_can_df = dl.tweets_beer_in_all_df[dl.tweets_beer_in_all_df['user_location'] == 'canberra']

    beer_info = pd.DataFrame(columns=['gcc_code16', 'gcc_name16', 'tweets_count', 'beer/all in city', 'beer/all beer'])

    beer_info.loc[0] = ['2GMEL','Greater Melbourne',len(beer_melb_df),len(beer_in_all_melb_df)/len(tweets_melb_df),len(beer_melb_df)/len(dl.beer_df)]
    beer_info.loc[1] = ['1GSYD','Greater Sydney',len(beer_syd_df),len(beer_in_all_syd_df)/len(tweets_syd_df),len(beer_syd_df)/len(dl.beer_df)]
    beer_info.loc[2] = ['3GBRI','Greater Brisbane',len(beer_bris_df),len(beer_in_all_bris_df)/len(tweets_bris_df),len(beer_bris_df)/len(dl.beer_df)]
    beer_info.loc[3] = ['4GADE','Greater Adelaide',len(beer_adel_df),len(beer_in_all_adel_df)/len(tweets_adel_df),len(beer_adel_df)/len(dl.beer_df)]
    beer_info.loc[4] = ['2GMEL','Greater Perth',len(beer_perth_df),len(beer_in_all_perth_df)/len(tweets_perth_df),len(beer_perth_df)/len(dl.beer_df)]
    beer_info.loc[5] = ['8ACTE','Australian Capital Territory',len(beer_can_df),len(beer_in_all_can_df)/len(tweets_can_df),len(beer_can_df)/len(dl.beer_df)]
    beer_info.loc[6] = ['nothing','Australia',len(dl.beer_df),len(dl.tweets_beer_in_all_df)/len(dl.df),len(dl.beer_df)/len(dl.beer_df)]

    print(beer_info)

    beer_json = beer_info.T.to_json()
    fileObject = open('./data/{}'.format('beer_analysis.json'), 'w')
    #fileObject = open('C:/Users/yanx5\Desktop/frontend_csv/{}'.format('beer_analysis.json'), 'w')
    fileObject.write(beer_json) 
    fileObject.close()