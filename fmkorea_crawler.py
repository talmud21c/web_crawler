import requests
from bs4 import BeautifulSoup

url = 'https://www.fmkorea.com/best/5147032699'

session = requests.Session()
session.get('https://www.fmkorea.com/best/5147032699')

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

webpage = requests.get(url, headers=headers)

soup = BeautifulSoup(webpage.content, 'lxml')

# 본문 내용 크롤링
article_title = soup.find('div', attrs={'class': 'xe_content'}).get_text().strip()
print(article_title)

nickname = soup.find('a', attrs={'class': 'nick'}).get_text().strip()
print(nickname)

elements = soup.find_all('b')

view_cnt = elements[0].string
print(view_cnt)

recommend_cnt = elements[1].string
print(recommend_cnt)

comment_cnt = elements[2].string
print(comment_cnt)

