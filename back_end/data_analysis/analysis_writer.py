import senti_analyzer as sa
import data_loader as dl
import beer_analysis as ba
import unhealthy_food_analysis as ufa
import percentage_calculator as pc
import language_count as lc
import pandas as pd
import numpy as np
import csv
import time

def loop_writers():
    while True:
        # all tweets senti analysis
        sa.sentiment_results_cal(dl.df,'all_senti_analysis.json')
        # has geo tweets senti analysis
        sa.sentiment_results_cal(dl.tweets_geo_df,'has_geo_senti_analysis.json')
        # covid tweets senti analysis
        sa.sentiment_results_cal(dl.df_covid,'covid_senti_analysis.json')
        # covid and vaccine tweets senti analysis
        sa.sentiment_results_cal(dl.tweets_covid_vaccine_df,'covid_vaccine_senti_analysis.json')
        # income senti analysis
        sa.sentiment_results_cal(dl.df_income,'income_analysis.json')
        # beer senti analysis
        ba.beer_analyzer()
        # unhealthy food analysis
        ufa.unhealthy_food_analyzer()
        # percentage of each senario
        pc.percentage_writer()
        # language count
        lc.language_counter()

        time.sleep(3600)

if __name__ == "__main__":
   loop_writers()



