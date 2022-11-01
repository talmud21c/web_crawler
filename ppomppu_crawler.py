import uglysoup


def main(url):
    soup = uglysoup.get_soup(url)

    # 제목
    article_title = soup.find('font', attrs={'class': 'view_title2'}).get_text().strip()

    # 작성자
    author = soup.find('font', attrs={'class': 'view_name'}).get_text().strip()

    # 작성일
    created_at = soup.find('div', attrs={'class': 'sub-top-text-box'}).find_all(text=True)[11]

    # 조회수
    view_cnt = soup.find('div', attrs={'class': 'sub-top-text-box'}).find_all(text=True)[12]

    # 추천수
    like_cnt = soup.select_one('#top_vote_item > strong').get_text().strip()

    # 본문 내용
    article = soup.find('td', attrs={'class': 'board-contents'}).get_text().strip()

    # 댓글 수
    comment_cnt = soup.find('span', attrs={'class': 'list_comment'}).get_text().strip()

    print(
        '제목: {}\n'.format(article_title),
        '작성자: {}\n'.format(author),
        '{}\n'.format(created_at),
        '{}\n'.format(view_cnt),
        '추천수: {}\n'.format(like_cnt),
        '본문 내용: {}\n'.format(article),
        '댓글 수: {}개\n'.format(comment_cnt)
    )

    # 댓글
    comments = []
    comment_all = soup.find_all('div', attrs={'class': 'over_hide'})
    for comment in comment_all:
        comments.append(comment.get_text().strip())
    print(comments)


if __name__ == '__main__':
    url_input = input('뽐뿌 게시글 url을 입력해 주세요: ')
    main(url_input)