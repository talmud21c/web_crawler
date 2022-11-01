import uglysoup


def main(url):
    soup = uglysoup.get_soup(url)

    # 본문 제목
    article_title = soup.find('span', attrs={'class': 'title'}).get_text().strip()

    # 작성자
    author = soup.find('div', attrs={'class': 'side'}).get_text().strip()

    # 작성일
    created_at = soup.find('div', attrs={'class': 'side fr'}).get_text().strip()

    # 본문 내용
    article = soup.find('article', attrs={'itemprop': 'articleBody'}).get_text().strip()

    # 조회 수
    view_cnt = soup.find('div', attrs={'class': 'count_container'}).get_text().strip()

    # 댓글 수 - [, ] 괄호 제거
    comment_cnt = soup.find('div', attrs={'class': 'comment_header_bar'}).get_text().strip()

    print(
        '제목: ' + article_title + '\n',
        '작성자: ' + author + '\n',
        '작성일: ' + created_at + '\n',
        '본문 내용: ' + article + '\n',
        '조회 수: ' + view_cnt + '\n',
        '댓글 수: ' + comment_cnt
    )

    # 댓글 - DC, 인벤과같이 POST를 통해 댓글 전송


if __name__ == '__main__':
    url_input = input('더쿠 게시글 url을 입력해주세요: ')
    main(url_input)