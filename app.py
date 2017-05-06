from flask import Flask
from flask import request
from flask import jsonify
import  json
from seventweets.seven.bridges.seventweets.Storage import Storage

app = Flask(__name__)



@app.route("/tweets/",methods=['POST'])
def add_tweet():
    print("DEBUG_N: add_tweet called")
    if not request.get_data():
        print("DEBUG_N: content error")
        return "Greska sadrzaja",400
    else:
        print("DEBUG_N: content ok")
        tweet = json.loads(request.get_data())
        Storage.add_tweet(tweet["tweet"])
        return "Uspesno dodat tweet",201


@app.route("/tweets/", methods=['GET'])
def get_tweets():
    print("DEBUG_N: get_tweets called")
    return Storage.get_tweets()


@app.route("/tweets/<tweet_id>",methods=['GET'])
def get_tweet_with_id(tweet_id):
    print("DEBUG_N: get_tweet_with_id called")
    return Storage.get_tweet_id(tweet_id)

@app.route("/tweets/<int:tweet_id>",methods=['DELETE'])
def delete_tweet(tweet_id):
    return Storage.delete_tweet_id(tweet_id)




if __name__ == "__main__":
    app.run()