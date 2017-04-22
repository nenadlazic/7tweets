import requests
import json

res = requests.get("http://127.0.0.1:5000/tweets_get_all")
print("Svi tweetovi -\n", res.text)
print("Status:", res.status_code)
# #
# #Get tweet by id
# req2 = requests.get("http://127.0.0.1:5000/tweets/2")
# print("Results:\n", req2.text)
# print("Status code:", req2.status_code)
#
#dodavanje novog tweet-a
# res = requests.post("http://127.0.0.1:5000/tweets", json={"tweet":"moj tvit 5"})
# print("Status:\n", res.text)
# print("Status code:", res.status_code)
#
# #Posting one more tweet
# pos2 = requests.post(url, json={"tweet":"This is tweet number 3"})
# print("Status code:", pos2.status_code)
# print("Status code:", pos2.status_code)
#
# #Deleting tweet by id
# dele = requests.delete("http://127.0.0.1:5000/tweets/4")
# print("Status\n", dele.text)
# print("Status code\n", dele.status_code)