import numpy as np
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

sentiment_word = []    
with open("AFINN-111.txt", "r") as s_word_file:
    for line in s_word_file.readlines():
        new_dic = {}
        line = line.strip('\n')
        line_list = line.split( )
        new_dic[line_list[0]]=line_list[1]
        sentiment_word.append(line_list)
        
sentiment_word_ap = []
for k in sentiment_word:
    more_word_list = []  
    if len(k) != 2:
        word = k[0]
        for i in range (1, len(k)-1):
            word = word + ' ' + k[i]
        more_word_list.append([word, int(k[-1])])
    else:
        sentiment_word_ap.append([k[0], int(k[1])])
    sentiment_word_ap = more_word_list + sentiment_word_ap
sentiment_word = sentiment_word_ap

sentiment_word_ap = {}
for k in sentiment_word:
    more_word_list = []  
    if len(k) != 2:
        word = k[0]
        for i in range (1, len(k)-1):
            word = word + ' ' + k[i]
        sentiment_word_ap[word] =  int(k[-1])
    else:
        sentiment_word_ap[k[0]] = int(k[1])

def sentiment_score_list(tweets, sentiment_word):
    score_list =[]
    for tweet in tweets:
        tweet_score = 0
        for word in tweet:
            if word in sentiment_word:
                tweet_score = tweet_score + sentiment_word[word]
        score_list.append(tweet_score)
    return score_list

import numpy as np
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

tt = TweetTokenizer()
stopwords = set(stopwords.words('english')) #note: stopwords are all in lowercase

def tokenize_lemmatize_tweets(tweets):
    
    tweets_tokenized = []    
    for tweet in tweets:
        tweet_tokenized = tt.tokenize(str(tweet))
        tweets_tokenized.append(tweet_tokenized)
        
    tweets_na_removed = []    
    for tweet_tokenized in tweets_tokenized:
        tweet_na_removed = []
        for word in tweet_tokenized:
            for element in word:
                if element.isalpha():
                    tweet_na_removed.append(word)
                    break
        tweets_na_removed.append(tweet_na_removed)
    
    tweets_lowercase = []    
    for tweet_na_removed in tweets_na_removed:
        tweet_lowercase = [word.lower() for word in tweet_na_removed]
        tweets_lowercase.append(tweet_lowercase)
    
    tweets_st_removed = []    
    for tweet_lowercase in tweets_lowercase:
        tweet_st_removed = []
        for word in tweet_lowercase:
            if word not in stopwords:
                tweet_st_removed.append(word)
        tweets_st_removed.append(tweet_st_removed)
    
    lemmatizer = WordNetLemmatizer()

    tweets_lemmatized = []    
    for tweet_st_removed in tweets_st_removed:
        tweet_lemmatized = []
        for word in tweet_st_removed:
            tweet_lemmatized.append(lemmatizer.lemmatize(word))
        tweets_lemmatized.append(tweet_lemmatized)
        
    return tweets_lemmatized

def neg_zero_pos_counter(ls):
    neg_count, zero_count, pos_count = 0, 0, 0
    for i in ls:
        if i > 0:
            pos_count += 1
        elif i == 0:
            zero_count += 1
        elif i < 0:
            neg_count += 1
    return neg_count, zero_count, pos_count


def senti_info_printer(texts, senti_words_dic):
    tokenized_texts = tokenize_lemmatize_tweets(texts)
    texts_score_list = sentiment_score_list(tokenized_texts, senti_words_dic)
    #print(np.mean(texts_score_list))
    #print(np.median(texts_score_list))
    #print(neg_zero_pos_counter(texts_score_list))
    return np.mean(texts_score_list), neg_zero_pos_counter(texts_score_list)


def df_avgs(df):
    favos = df['favorite_count']
    followers = df['followers_count']
    favos = favos.replace('nothing',0)
    followers = followers.replace('nothing',0)
    avg_favo =favos.astype(float).mean()
    avg_follower = followers.astype(float).mean()
    return avg_favo, avg_follower