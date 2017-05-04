import requests
import json



#testiranje dodavanje tweet-a
# r = requests.post(
#     url='http://127.0.0.1:5000/tweets/',
#     json={'tweet':'Juventus osvaja Ligu Sampiona'}
# )
# print("Status:",r.status_code)

#testiranje citanja svih tweetova
r = requests.get(
    url='http://127.0.0.1:5000/tweets/'
)
print("Status:",r.status_code)
print(r.text)

#testiranje citanja tweet-a sa zadatim id-om
# r = requests.get(
#     url='http://127.0.0.1:5000/tweets/1'
# )
# print("Status:",r.status_code)
# print(r.text)

#testiranje brisanja tweet-a sa zadatim id-om
# r = requests.delete(
#     url='http://127.0.0.1:5000/tweets/1'
# )
# print("Status:",r.status_code)
# print(r.text)



def upload_my_tweets():
    with open('my_tweets.txt', encoding="utf8") as f:
        for line in f:
            print(line)
            r = requests.post(
                url='http://127.0.0.1:5000/tweets/',
                json={'tweet': line}
            )
            print("Status:", r.status_code)

# upload_my_tweets()