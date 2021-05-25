import pandas as pd
import data_loader as dl

def language_counter():
    language_count = dl.df['language'].value_counts()

    columns = ['count_or_percentage','English','Indian','Japanese','Spanish','Arabic','Tagalog','Portuguese','Chinese','Turkish','French','all']
    counts_df = pd.DataFrame(columns=columns)
    counts_df.loc[0] = ['count',
                        language_count.loc['en'],
                        language_count.loc['in']+language_count.loc['hi'],
                        language_count.loc['ja'],
                        language_count.loc['es'],
                        language_count.loc['ar'],
                        language_count.loc['tl'],
                        language_count.loc['pt'],
                        language_count.loc['zh'],
                        language_count.loc['tr'],
                        language_count.loc['fr'],
                        len(dl.df)-language_count.loc['und']]
    counts_df.loc[1] = ['percentage',
                        language_count.loc['en']/(len(dl.df)-language_count.loc['und']),
                        (language_count.loc['in']+language_count.loc['hi'])/(len(dl.df)-language_count.loc['und']),
                        language_count.loc['ja']/(len(dl.df)-language_count.loc['und']),
                        language_count.loc['es']/(len(dl.df)-language_count.loc['und']),
                        language_count.loc['ar']/(len(dl.df)-language_count.loc['und']),
                        language_count.loc['tl']/(len(dl.df)-language_count.loc['und']),
                        language_count.loc['pt']/(len(dl.df)-language_count.loc['und']),
                        language_count.loc['zh']/(len(dl.df)-language_count.loc['und']),
                        language_count.loc['tr']/(len(dl.df)-language_count.loc['und']),
                        language_count.loc['fr']/(len(dl.df)-language_count.loc['und']),
                        1]
    

    print(counts_df)

    language_count_json = counts_df.T.to_json()
    fileObject = open('./data/{}'.format('language_count.json'), 'w')
    #fileObject = open('C:/Users/yanx5\Desktop/frontend_csv/{}'.format('language_count.json'), 'w')
    fileObject.write(language_count_json) 
    fileObject.close()


