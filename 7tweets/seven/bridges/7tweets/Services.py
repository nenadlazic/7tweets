from flask import Flask
from flask import request
from flask import jsonify
import  json
from Storage import Storage

app = Flask(__name__)

@app.route("/tweets_get_all/",methods=['GET'])
def get_tweets():
    tweet = Storage.get_tweets()
    return "dadasdadad" if tweet else ("Nema twitova", 404)


@app.route("/tweets/<int:tweet_id>",methods=['GET'])
def get_tweet(tweet_id):
    return jsonify(Storage.get_tweet(tweet_id))


@app.route("/tweets",methods=['POST'])
def add_tweet():
    if not request.get_data():
        return "Greska sadrzaja"
    else:
        tweet = json.loads(request.get_data())
        Storage.add_tweet(tweet["tweet"])
        return "Uspesno dodat tweet", 201


@app.route("/tweets/<int:tweet_id>",methods=['DELETE'])
def delete_tweet(tweet_id):
    return jsonify(Storage.delete_tweet(tweet_id)),204




if __name__ == "__main__":
    app.run()