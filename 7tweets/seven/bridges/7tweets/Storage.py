from flask import jsonify
import json
"""
Modul which contains storage for tweets
"""

class Storage(object):
    _tweets = []
    tweet_count = 0
    name = "nlazic"

    #klasni metod za dodavanje tweet-a u storage
    @classmethod
    def add_tweet(cls,tweet_content):
        print("DEBUG_N: add_tweet called in Storage class")
        cls.tweet_count = cls.tweet_count+1
        new_tweet = {"tweet_id":cls.tweet_count, "name":cls.name, "tweet":tweet_content}
        cls._tweets.append(new_tweet)
        print("DEBUG_N: all tweets ",cls._tweets)

    @classmethod
    def get_tweets(cls):
        res = "Svi tvitovi korisnika nlazic: \n"
        res += "\n"
        print(cls._tweets)
        for t in cls._tweets:
            print(t)
            s = json.dumps(t)
            print(s)
            res +=s
            res += "\n"

        if cls._tweets.__len__() == 0:
            return "Nema tweetova"
        else:
            print("DEBUG_N: vracam rezultat ",res)
            return res

    @classmethod
    def get_tweet_id(cls, tweet_id):
        print("DEBUG_N: get_tweet_id called")
        print("id: ",tweet_id)

        res = "Tweet sa id-om "+tweet_id
        res += "\n"
        for tweet in cls._tweets:
            print(tweet['tweet_id'])
            x = int(tweet['tweet_id'])
            print(type(x))
            print(type(tweet_id))

            if x == int(tweet_id):
                return res+json.dumps(tweet)
        else:
            return "Ne postoji tweet sa zadatim id-om"



    @classmethod
    def delete_tweet_id(cls, tweet_id):
        print("DEBUG_N: delete_tweet_id called")

        i = 0
        for tweet in cls._tweets:
            x = int(tweet['tweet_id'])
            if x == int(tweet_id):
                del cls._tweets[i]
                return "Tweet je uspesno obrisan"
            i+=1
        else:
            return "Ne postoji tweet sa zadatim id-om"
