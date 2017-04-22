from flask import jsonify
import json
"""
Modul which contains storage for tweets
"""

class Storage(object):
    _tweets = []
    tweet_id = 0;
    tweet_count = 1;
    name = "Nenad Lazic";
    tweet_default = {"id": tweet_id, "name": name, "tweet": "Pozdrav svima."}

    @classmethod
    def get_tweets(cls):
        res = "svi tvitovi: "
        for t in cls._tweets:
            json_string = json.dumps(t)
            res = res + json_string

        return res

    @classmethod
    def get_tweet(cls, tweet_id):
        for tweet in cls._tweets:
            if tweet['id'] == tweet_id:
                return tweet
        else:
            return "Ne postoji tweet sa zadatim id-om"

    @classmethod
    def add_tweet(cls,tweet_content):
        cls.tweet_count = cls.tweet_count+1
        new_tweet = {id:cls.tweet_count, "name":cls.name, "tweet":tweet_content}
        cls._tweets.append(new_tweet)

    @classmethod
    def delete_tweet(cls, tweet_id):
        i = 0
        for tweet in cls._tweets:
            if tweet["id"] == tweet_id:
                del cls._tweets[i]
                return "Tweet je uspesno obrisan"
            i+=1
        else:
            return "Ne postoji tweet sa zadatim id-om"


    @classmethod
    def del_tweet(cls, tweet_id):
        for tweet in cls._tweets:
            if tweet['id'] == tweet_id:
                cls._tweets.remove(tweet)
        else:
            return None

    @classmethod
    def delete_all(cls):
        del cls._tweets


