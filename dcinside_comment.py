import requests
from bs4 import BeautifulSoup
import websocket
import time
import json

url = 'https://gall.dcinside.com/board/comment/'


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

response = requests.post(url, payload)
print(response)

soup = BeautifulSoup(response.content, 'lxml')
print(soup.text)

