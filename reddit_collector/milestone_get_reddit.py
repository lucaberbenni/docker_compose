import requests
from requests.auth import HTTPBasicAuth
import sys
from config import tokens
import pymongo

sys.stdout.reconfigure(encoding='utf-8')
client = pymongo.MongoClient(host = 'mongodb', port = 27017)
db = client.reddit

basich_auth = HTTPBasicAuth(
    username=tokens['client_id'], 
    password=tokens['secret']
)

GRANT_INFORMATION = dict(
    grant_type='password', 
    username = tokens['username'], 
    password = tokens['password']
)

headers = {
    'User-Agent' : 'Mozilla'
}

POST_URL = 'https://www.reddit.com/api/v1/access_token'

access_post_response = requests.post(
    url=POST_URL, 
    headers=headers, 
    data=GRANT_INFORMATION, 
    auth=basich_auth
).json()

headers['Authorization'] = access_post_response['token_type'] + ' ' + access_post_response['access_token']

topic = 'artificial'
URL = f"https://oauth.reddit.com/r/{topic}/hot"

response = requests.get(
    url=URL, 
    headers=headers
).json()

full_response = response['data']['children']

collection = db.posts

for post in full_response:
    _id = post['data']['id']
    title = post['data']['title']
    mongo_input = {'_id' : _id, 'text' : title}
    collection.insert_one(mongo_input)