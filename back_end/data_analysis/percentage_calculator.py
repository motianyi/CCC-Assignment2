import pandas as pd
import data_loader as dl

def percentage_writer():
    percentages = []

    covid_p = len(dl.tweets_covid_in_all_df) / len(dl.df)

    covid_vaccine_in_all_df = dl.tweets_covid_in_all_df[dl.tweets_covid_in_all_df['text'].str.contains('vaccine')]
    covid_vaccine_p = len(covid_vaccine_in_all_df) / len(dl.df)

    unhealthy_food_p = len(dl.tweets_unhealthy_df) / len(dl.df)

    beer_p = len(dl.tweets_beer_in_all_df) / len(dl.df)

    income_p = len(dl.tweets_income_in_all_df) / len(dl.df)

    percentages = [covid_p,covid_vaccine_p,unhealthy_food_p,beer_p,income_p]

    senario_percentage_df = pd.DataFrame(columns=['scenario', 'percentage'])

    senario_percentage_df['scenario'] = ['covid','covid_vaccine','unhealthy_food','beer','income']
    senario_percentage_df['percentage'] = percentages

    print(senario_percentage_df)

    senario_percentage_json = senario_percentage_df.T.to_json()
    fileObject = open('./data/{}'.format('senario_percentage.json'), 'w')
    #fileObject = open('C:/Users/yanx5\Desktop/frontend_csv/{}'.format('senario_percentage.json'), 'w')
    fileObject.write(senario_percentage_json) 
    fileObject.close() 





