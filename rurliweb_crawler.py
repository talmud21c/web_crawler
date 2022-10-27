import uglysoup


def main(url):
    soup = uglysoup.get_soup(url)

    # 본문 제목
    article_title = soup.find('span', attrs={'class': 'subject_inner_text'}).get_text().strip()
    print(article_title)

    # 작성자
    nickname = soup.find('strong', attrs={'class': 'nick'}).get_text().strip()
    print(nickname)

    # 작성일
    created_at = soup.find('span', attrs={'class': 'regdate'}).get_text().strip()
    print(created_at)

    # 작성자 IP - ip span 태그에 css class가 없으므로 css 선택자 사용
    ip_address = soup.select_one('div.col.user_info_wrapper > div > p:nth-child(7) > span').get_text().strip()
    print(ip_address)

    # 본문 내용
    article = soup.find('article', attrs={'class': None}).get_text().strip()
    print(article)

    # 추천 수
    recommend_cnt = soup.find('span', attrs={'class': 'like'}).get_text().strip()
    print(recommend_cnt)

    # 조회 수
    # soup.find('div', attrs={'class': 'user_info'})
    view_cnt_new = soup.head.contents
    print(view_cnt_new)

    view_cnt = soup.find('span', attrs={'class': 'like'}).next_sibling.next_sibling.next_sibling
    print('조회수: ' + view_cnt)

    # 댓글 수 - [, ] 괄호 제거
    comment_cnt_bucket = soup.find('strong', attrs={'class': 'reply_count'}).get_text().strip()
    comment_cnt = str(comment_cnt_bucket)[1:-1]
    print(comment_cnt)

    print(article_title)


if __name__ == '__main__':
    webpage_url = 'https://bbs.ruliweb.com/best/board/300143/read/59056711'
    main(webpage_url)
