import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd

url = 'https://gall.dcinside.com/board/view/?id=programming&no=1476608&page=1'

session = requests.Session()
session.get('https://gall.dcinside.com/board/view/?id=programming&no=1476608&page=1')

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

webpage = requests.get(url, headers=headers)

soup = BeautifulSoup(webpage.content, 'lxml')


# ---------------------------본문 내용 출력 테스트-----------------------------------------
article_title = soup.find('span', attrs={'class': 'title_subject'}).get_text().strip()

nickname = soup.find('span', attrs={'class': 'nickname'}).get_text().strip()

ip_address = soup.find('span', attrs={'class': 'ip'}).get_text().strip()

view_cnt = soup.find('span', attrs={'class': 'gall_count'}).get_text().strip()

comment_cnt = soup.find('span', attrs={'class': 'gall_comment'}).get_text().strip()
cmt_cnt = comment_cnt.replace('댓글', '')
print(int(cmt_cnt))

content_all = soup.find('div', attrs={'class': 'writing_view_box'})
content = content_all.p.get_text().strip()

reg_dtime = soup.find('span', attrs={'class': 'gall_date'}).get_text().strip()

article_data = (article_title, nickname, ip_address, view_cnt, comment_cnt, content, reg_dtime)
print(article_data)

# ---------------------------댓글 출력 테스트----------------------------------
comments = []
comment_elements = soup.find_all('li', attrs={'class': 'ub-content'})
print(comment_elements)

nickname_all = soup.find_all(class_='ub-writer')
print(nickname_all)

for element in comment_elements:
    nickname = soup.find('em', attrs={'title': '닉네임'})
    body = element.find('p', attrs={'class': 'ub-word'})
    user_ip = '' if nickname else body.find('span').extract().text
    timestamp = element.find('span', attrs={'class': 'date_time'}).text

    comment = {
        'user_ip': user_ip,
        'nickname': nickname,
        'written_at': timestamp,
        'body': body.text.strip()
    }

    comments.append(comment)

print(comments)