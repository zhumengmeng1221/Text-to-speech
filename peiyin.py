#coding=utf-8
from aip import AipSpeech
 

APP_ID = '16804374'
API_KEY = 'VXPqfIZzDbsqpwTi4IGq3Xsc'
SECRET_KEY = 'XzrZaNA0nhKo0IEDexYC43IbjImI6esw'
 
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
 
result  = client.synthesis('你的文字', 'zh', 1, {'vol': 5,'per':1
})
 
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)

print("配音成功")
