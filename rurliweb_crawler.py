import uglysoup


def main(url):
    soup = uglysoup.get_soup(url)

    # 본문 제목
    article_title = soup.find('span', attrs={'class': 'subject_inner_text'}).get_text().strip()

    # 작성자
    nickname = soup.find('strong', attrs={'class': 'nick'}).get_text().strip()

    # 작성일
    created_at = soup.find('span', attrs={'class': 'regdate'}).get_text().strip()

    # 작성자 IP - ip span 태그에 css class가 없으므로 css 선택자 사용
    ip_address = soup.select_one('div.col.user_info_wrapper > div > p:nth-child(7) > span').get_text().strip()

    # 본문 내용
    article = soup.find('article', attrs={'class': None}).get_text().strip()

    # 추천 수
    recommend_cnt = soup.find('span', attrs={'class': 'like'}).get_text().strip()

    # 조회 수
    # soup.find('div', attrs={'class': 'user_info'})
    view_cnt_new = soup.title.contents
    print(view_cnt_new)

    view_cnt = soup.find('span', attrs={'class': 'like'}).next_sibling.next_sibling.next_sibling
    print('조회수: ' + view_cnt)

    # 댓글 수 - [, ] 괄호 제거
    comment_cnt_bucket = soup.find('strong', attrs={'class': 'reply_count'}).get_text().strip()
    comment_cnt = str(comment_cnt_bucket)[1:-1]

    print('제목: ' + article_title + '\n',
          '작성자: ' + nickname + '\n',
          '작성일: ' + created_at + '\n',
          '작성자 IP: ' + ip_address + '\n',
          '본문 내용: ' + article + '\n',
          '추천 수: ' + recommend_cnt + '\n',
          '조회 수: ' + view_cnt + '\n',
          '댓글 수: ' + comment_cnt)

    # 댓글
    comments = []
    comment_all = soup.find_all('span', attrs={'class': 'text'})
    for comment in comment_all:
        comments.append(comment.get_text().strip())
    print(comments)


if __name__ == '__main__':
    url_input = input('루리웹 게시글 url을 입력해주세요: ')
    main(url_input)
