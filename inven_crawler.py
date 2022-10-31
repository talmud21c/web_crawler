import uglysoup


def main(url):
    soup = uglysoup.get_soup(url)

    # 기사 제목
    article_title = soup.find('span', attrs={'class': 'category'}).next_sibling

    # 작성자
    author = soup.find('div', attrs={'class': 'writer'}).get_text().strip()

    # 작성 날짜
    created_at = soup.find('dd').get_text().strip()

    # 본문 내용
    article = soup.find('div', attrs={'class': 'contentBody'}).get_text().strip()

    # 추천 수
    # like_cnt = soup.find('button', attrs={'class': 'btn_share_like'}).get_text().strip()

    # 댓글 수
    comment = soup.find('span', attrs={'class': 'cmtContentOne'}).get_text().strip()

    print('제목: ' + article_title + '\n',
          '작성자: ' + author + '\n',
          '작성일: ' + created_at + '\n',
          '본문 내용: ' + article + '\n',
          '댓글: ' + comment + '\n',)

if __name__ == '__main__':
    website_url = 'https://www.inven.co.kr/webzine/news/?news=278114'
    main(website_url)