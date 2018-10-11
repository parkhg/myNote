## parser.py
import requests
from bs4 import BeautifulSoup
import json
import os
import sys

## python file의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

## 게시판 가져오기
req = requests.get('http://beomi.github.io/beomi.github.io_old/')
# req = requests.get('http://www.wu.ac.kr/wu/1353/subview.do')


## http Status 가져오기(200:정상)
status = req.status_code
print(status)

html = req.text
print(html)
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'h3 > a'
)

data = {}

for title in my_titles:
    data[title.text] = title.get('href')
    print(title.text)

## encoding 확인
sys_encoding = sys.getdefaultencoding()
print("system encoding : ", sys_encoding)

print(data)

with open(os.path.join(BASE_DIR, 'result.json'),'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file)

## To Do List
"""
1. 제목을 click하여 해당 게시판으로 이동(URL)
2. 제목을 단어로 Split하여 Word Cloud를 만든다.
3. URL을 외부로부터 Parameter로 받아서 처리한다.
4. Error처리 보완
"""
