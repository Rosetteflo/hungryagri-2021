import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.modunong.or.kr:449/contents/garden/gardenList.do?menuNo=17',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.hungryagri

# 코딩 시작

lis = soup.select('#listForm > div.cont_area > div.plan > ul > li')

for li in lis:
    title=li.select_one('a > div.tp > div.subj').text
    address = li.select_one('a > ul > li.addr').text
    area= li.select_one('a > ul > li.phone').text
    phone = li.select_one('a > ul > li.area').text
    price = li.select_one('a > ul > li.price').text

doc = {'tilte':title,
       'address':address,
       'area':area,
       'phone':phone,
       'price':price
       }
db.harvest.insert_one(doc)

