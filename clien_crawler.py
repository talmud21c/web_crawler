import uglysoup


def main(url):
    soup = uglysoup.get_soup(url)

    # 제목
    title = soup.select_one('h3 > span').get_text().strip()

    # 작성자
    author = soup.find('span', attrs={'class': 'nickname'}).get_text().strip()

    # 작성일
    created_at = soup.find('span', attrs={'class': 'fa-clock-o'}).next_sibling

    # 조회수
    view_cnt = soup.find('strong').get_text().strip()

    # 추천수(공감)
    like_cnt = soup.select_one('a > strong').get_text().strip()

    # 본문 내용
    article = soup.find('div', attrs={'class': 'post_article'}).get_text().strip()

    # 댓글수
    comment_cnt = soup.select_one("#comment-point > a > strong").get_text().strip()

    print(
        '제목: {}\n'.format(title),
        '작성자: {}\n'.format(author),
        '작성일: {}\n'.format(created_at),
        '조회수: {}\n'.format(view_cnt),
        '추천수: {}\n'.format(like_cnt),
        '본문 내용: {}\n'.format(article),
        '댓글수: {}\n'.format(comment_cnt)
    )

    # 댓글
    comments = []
    comment_all = soup.find_all('div', attrs={'class': 'comment_view'})
    for comment in comment_all:
        comments.append(comment.get_text().strip())
    print(comments)


if __name__ == '__main__':
    url_input = 'https://www.clien.net/service/board/park/17678695?od=T33&po=0&category=0&groupCd='
    main(url_input)