import pandas as pd
import numpy as np
import csv
import calculators as ca
import json

def sentiment_results_cal(df,csvfile,jsonfile):

    #print(df)
    texts_all = df['text']
    aus_senti_info = ca.senti_info_printer(texts_all, ca.sentiment_word_ap)

    tweets_melb_df = df[df['user_location'] == 'melbourne']
    tweets_syd_df = df[df['user_location'] == 'sydney']
    tweets_bris_df = df[df['user_location'] == 'brisbane']
    tweets_adel_df = df[df['user_location'] == 'adelaide']
    tweets_perth_df = df[df['user_location'] == 'perth']
    tweets_can_df = df[df['user_location'] == 'canberra']
    #tweets_rest_df = df[df['user_location'] != 'melbourne' and df['user_location'] != 'sydney' and df['user_location'] != 'brisbane' and df['user_location'] != 'adelaide' and df['user_location'] != 'perth']

    texts_melb_df = tweets_melb_df['text']
    texts_syd_df = tweets_syd_df['text']
    texts_bris_df = tweets_bris_df['text']
    texts_adel_df = tweets_adel_df['text']
    texts_perth_df = tweets_perth_df['text']
    texts_can_df = tweets_can_df['text']
    #texts_rest_df = tweets_rest_df['text']


    melb_senti_info = ca.senti_info_printer(texts_melb_df, ca.sentiment_word_ap)
    syd_senti_info = ca.senti_info_printer(texts_syd_df, ca.sentiment_word_ap)
    bris_senti_info = ca.senti_info_printer(texts_bris_df, ca.sentiment_word_ap)
    adel_senti_info = ca.senti_info_printer(texts_adel_df, ca.sentiment_word_ap)
    perth_senti_info = ca.senti_info_printer(texts_perth_df, ca.sentiment_word_ap)
    can_senti_info = ca.senti_info_printer(texts_can_df, ca.sentiment_word_ap)



    #senti_info_list = [aus_senti_info,melb_senti_info,syd_senti_info,bris_senti_info,adel_senti_info,perth_senti_info,can_senti_info]

    all_senti_info = pd.DataFrame(columns=['gcc_code16', 'gcc_name16', 'senti_score', 'num_neg', 'num_neu', 'num_posi','tweets_count'])

    all_senti_info.loc[0] = ['2GMEL','Greater Melbourne',melb_senti_info[0],melb_senti_info[1][0],melb_senti_info[1][1],melb_senti_info[1][2],len(texts_melb_df)]
    all_senti_info.loc[1] = ['1GSYD','Greater Sydney',syd_senti_info[0],syd_senti_info[1][0],syd_senti_info[1][1],syd_senti_info[1][2],len(texts_syd_df)]
    all_senti_info.loc[2] = ['3GBRI','Greater Brisbane',bris_senti_info[0],bris_senti_info[1][0],bris_senti_info[1][1],bris_senti_info[1][2],len(texts_bris_df)]
    all_senti_info.loc[3] = ['4GADE','Greater Adelaide',adel_senti_info[0],adel_senti_info[1][0],adel_senti_info[1][1],adel_senti_info[1][2],len(texts_adel_df)]
    all_senti_info.loc[4] = ['2GMEL','Greater Perth',perth_senti_info[0],perth_senti_info[1][0],perth_senti_info[1][1],perth_senti_info[1][2],len(texts_perth_df)]
    all_senti_info.loc[5] = ['8ACTE','Australian Capital Territory',can_senti_info[0],can_senti_info[1][0],can_senti_info[1][1],can_senti_info[1][2],len(texts_can_df)]
    all_senti_info.loc[6] = ['nothing','Australia',aus_senti_info[0],aus_senti_info[1][0],aus_senti_info[1][1],aus_senti_info[1][2],len(texts_all)]

    print(all_senti_info)

    all_senti_info.to_csv (r'C:/Users/yanx5\Desktop/frontend_csv/{}'.format(csvfile), index = False, header=True)

    senti_json = all_senti_info.T.to_json()
    fileObject = open('C:/Users/yanx5\Desktop/frontend_csv/{}'.format(jsonfile), 'w')
    fileObject.write(senti_json) 
    fileObject.close()