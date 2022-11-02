import uglysoup


def main(url):
    soup = uglysoup.get_soup(url)

    # 제목
    title = soup.find('span', attrs={'id': 'ai_cm_title'}).get_text().strip()

    # 작성자
    author = soup.find('span', attrs={'class': 'hu_nick_txt'}).get_text().strip()

    # 작성일
    created_at = soup.select_one('#if_date > span:nth-child(1)').get_text().strip()

    # 조회수
    view_cnt = soup.select_one('#content_info > span:nth-child(9)').get_text().strip()

    # 추천수
    like_cnt = soup.find('span', attrs={'id': 'ok_div'}).get_text().strip()

    # 본문 내용
    article = soup.find('div', attrs={'id': 'wrap_body'}).get_text().strip()

    # 댓글수
    comment_cnt = soup.find('span', attrs={'class': 're'}).get_text().strip()

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
    best_comments = []
    best_comment_all = soup.select('span.cmt_text')
    for comment in best_comment_all:
        best_comments.append(comment.get_text().strip())
    print(best_comments)

    # document.querySelector("#comment_span_169421878 > td:nth-child(3)")
    common_comments = []
    common_comment_all = soup.find_all('span', attrs={'class': 'cmt_list'})
    for comment in common_comment_all:
        common_comments.append(comment.get_text().strip())
    print(common_comments)


if __name__ == '__main__':
    # url_input = input('웃긴대학 게시글 url을 입력해 주세요: ')
    url_input = 'http://web.humoruniv.com/board/humor/read.html?table=pick&pg=0&number=1190565'
    main(url_input)