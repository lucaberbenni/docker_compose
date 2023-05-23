import requests
import sys
from config import tokens
from sqlalchemy import create_engine, text
import time

time.sleep(20)

webhook_url = tokens['webhook_url']

pg = create_engine('postgresql://docker_user:12345@postgresdb:5432/reddit', echo = True)
pg_connect = pg.connect()

text = text('''
    SELECT *
    FROM posts
    WHERE sentiment < 0 
    ORDER BY sentiment ASC LIMIT 1;
''')

text_sql = pg_connect.execute(text)
post = text_sql.fetchall()

data = {'text': f'{post[0][0]}, {post[0][1]}'}

requests.post(url=webhook_url, json= data)

pg_connect.close()