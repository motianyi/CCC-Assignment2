import requests
import os
import json
import sys
import tweepy

def authorization(bearer_token):
    header = {"Authorization":"Bearer {}".format(bearer_token)}
    return header


def get_rules(header_value):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", headers=header_value
    )

    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code,response.text)   
        )

    print(json.dumps(response.json()))
    return response.json()


def add_rules(header_value,rules):
    payload = {"add": rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=header_value,
        json=payload
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def delete_rules(header_value,rule_id_list):
    payload = {"delete":{"ids":rule_id_list}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=header_value,
        json=payload
    )

    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code,response.text)   
        )

    print(json.dumps(response.json()))
    

def get_stream(header_value):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", headers=header_value, stream=True
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code,response.text)   
        )  

    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))


def get_stream_limited(header_value,max_tweets_num):
    tweet_num = 0
    result_list = []
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", headers=header_value, stream=True
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code,response.text)   
        )  

    for response_line in response.iter_lines():

        tweet_num += 1
        if tweet_num >= max_tweets_num:
            #sys.exit()
            break

        if response_line:

            json_response = json.loads(response_line)
            result_list.append(json_response)
            print(json.dumps(json_response, indent=4, sort_keys=True))
    
    return result_list


def write_json(file_path,content):
    with open(file_path,"w") as f:
        json.dump(content,f)
        print("write json successfully")

def load_json(file_path):
    with open(file_path,"r") as f:
        result = json.load(f)
        print("load json successfully")
    return result


def get_tweet(key_word_list,geocode_value,tweet_num,twitter_api):
   result_list = []
   for item in key_word_list:
      cricTweets = tweepy.Cursor(twitter_api.search, q=item, geocode=geocode_value).items(tweet_num)
      result_list.append(cricTweets)

   return result_list


def get_apiaccess(consumer_key,consumer_secret,access_token,access_token_secret):
    # authorization of consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # set access to user's access key and access secret 
    auth.set_access_token(access_token, access_token_secret)
    # calling the api 
    api = tweepy.API(auth)

    return api