import pymongo
import time
from sqlalchemy import create_engine, text
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

time.sleep(10)

client = pymongo.MongoClient(host='mongodb', port= 27017)

db = client.reddit

pg = create_engine('postgresql://docker_user:12345@postgresdb:5432/reddit', echo = True)
pg_connect = pg.connect()

create_table = text('''
    CREATE TABLE IF NOT EXISTS posts (
    text VARCHAR(500),
    sentiment NUMERIC);
''')

pg_connect.execute(create_table)
pg_connect.commit()

docs = db.posts.find()

analyzer = SentimentIntensityAnalyzer()

for doc in docs:
    title= doc['text'].replace("'", " ")
    score = analyzer.polarity_scores(doc['text'])['compound']
    insert = text(f"INSERT INTO posts VALUES ('{title}', {score});")
    pg_connect.execute(insert)
    pg_connect.commit()

pg_connect.close()