import requests
from bs4 import BeautifulSoup

# naver 뉴스 랭킹 url - 댓글 많은 뉴스
url = 'https://news.naver.com/main/ranking/popularMemo.naver'

# 크롤링을 차단을 피하기 위해 헤더 정보 삽입
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# 페이지 요청
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'lxml')

ranking_boxes = soup.find_all('div', 'rankingnews_box')

ranking_news_titles = []

for ranking_box in ranking_boxes:
    article_list = ranking_box.find('ul', 'rankingnews_list').find_all('li')
    for arti in article_list:
        content = arti.find('div', 'list_content')
        if content:
            ranking_news_titles.append(content.find('a').text.strip())

for title in ranking_news_titles:
    print(title)

# tag.media_end_head_headline