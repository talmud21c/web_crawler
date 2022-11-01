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

    # 추천 수 - 버튼형식으로 만들어져 추출 시도중
    # like_cnt = soup.select_one('#webzineNewsView > div.newsPart > div.news_share_area > div.share_area > button.btn_share.like').get_text().strip()

    # 댓글 수
    comment = soup.select_one('#webzineNewsView > div.newsPart > div.topinfo > dl.comment > dd').get_text().strip()

    print('제목: ' + article_title + '\n',
          '작성자: ' + author + '\n',
          '작성일: ' + created_at + '\n',
          '본문 내용: ' + article + '\n',
          '댓글: ' + comment + '\n',)

    # 댓글 - DC인사이드와 같이 POST형식으로 댓글 전송받음


if __name__ == '__main__':
    url_input = input('인벤 기사 url을 입력해 주세요: ')
    main(url_input)