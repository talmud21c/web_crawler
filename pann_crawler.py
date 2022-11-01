import uglysoup


def main(url):
    soup = uglysoup.get_soup(url)

    # 제목
    article_title = soup.find('h4').get_text().strip()

    # 작성자
    author = soup.find('a', attrs={'class': 'writer'}).get_text().strip()

    # 본문 내용
    article = soup.find(id='contentArea').get_text().strip()

    # 작성일
    created_at = soup.find('span', attrs={'class': 'date'}).get_text().strip()

    # 조회
    view_cnt = soup.find('span', attrs={'class': 'count'}).get_text().strip()

    # 추천
    like_cnt = soup.select_one('div.updown.f_clear > div > div.btnbox.up > span').get_text().strip()

    # 댓글 수
    comment_cnt = soup.find('strong').get_text().strip()

    print('제목: ' + article_title + '\n',
          '작성자: ' + author + '\n',
          '본문 내용: ' + article + '\n',
          '작성일: ' + created_at + '\n',
          '조회수: ' + view_cnt + '\n',
          '추천수: ' + like_cnt + '\n',
          '댓글수: ' + comment_cnt + '\n',
          )

    # 댓글
    comments = []
    comment_all = soup.find_all('dd', attrs={'class': 'usertxt'})
    for comment in comment_all:
        comments.append(comment.get_text().strip())
    print(comments)


if __name__ == '__main__':
    url_input = input('네이트 판 게시글 url을 입력하세요: ')
    main(url_input)