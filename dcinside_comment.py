import urllib.parse
from urllib.request import Request

import requests
from bs4 import BeautifulSoup
import websocket
import time
import json

url = 'https://gall.dcinside.com/board/comment/'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01'
    }

session = requests.Session()
session.post(url)

payload = {
    'id': 'dcbest',
    'no': 87585,
    'cmt_id': 'dcbest',
    'cmt_no': 87585,
    'focus_cno': '',
    'focus_pno': '',
    'e_s_n_o': '3eabc219ebdd65f23d',
    'comment_page': 1,
    'sort': 'D',
    'prevCnt': 0,
    'board_type': '',
    '_GALLTYPE': 'G'
}

# 페이로드 인코딩
# payload = urllib.parse.urlencode(payload)
# payload = payload.encode('utf-8')
# print(payload)

response = requests.post(url, data=payload, headers=headers)
print(response)

soup = BeautifulSoup(response.content, 'lxml')
print(soup)

