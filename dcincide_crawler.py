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

article_title = soup.find('span', attrs={'class':'title_subject'}).get_text().strip()

nickname = soup.find('span', attrs={'class':'nickname'}).get_text().strip()

ip_address = soup.find('span', attrs={'class':'ip'}).get_text().strip()

view_cnt = soup.find('span', attrs={'class':'gall_count'}).get_text().strip()

comment_cnt = soup.find('span', attrs={'class':'gall_comment'}).get_text().strip()

content_all = soup.find('div', attrs={'class': 'writing_view_box'})
content = content_all.p.get_text().strip()

reg_dtime = soup.find('span', attrs={'class':'gall_date'}).get_text().strip()

article_data = (article_title, nickname,
                ip_address, view_cnt, comment_cnt, content, reg_dtime)

print(article_data)

f = open('dc_crawling_result.csv', 'a', encoding='utf8')
for i in article_data:
    f.write(str(i) + ", ")
f.close()

# xpath 방식 접근 실패 (BeautifulSoup 공식 지원 X)
# dom = etree.HTML(str(soup))
# print(dom.xpath('//*[@id="container"]/section/article[2]/div[1]/div/div[1]/div[1]/div[3]/p')[0].text)


# # XPath
# //*[@id="container"]/section/article[2]/div[1]/div/div[1]/div[1]/div[3]/p
# # JS 경로
# document.querySelector("#container > section > article:nth-child(3) > div.view_content_wrap > div > div.inner.clear > div.writing_view_box > div.write_div > p")
# # selector
# #container > section > article:nth-child(3) > div.view_content_wrap > div > div.inner.clear > div.writing_view_box > div.write_div > p