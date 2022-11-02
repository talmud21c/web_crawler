import uglysoup


def main(url):
    soup = uglysoup.get_soup(url)

    # 제목
    title = soup.find('strong', attrs={'itemprop': 'name'}).get_text().strip()
    title = title[:-4]

    # 작성자
    author = soup.find('a', attrs={'class': 'nickName'}).get_text().strip()

    # 작성일
    created_at = soup.select_one('#print_area > div.writerProfile > dl > dt > span > em:nth-child(4)').next_sibling

    # 조회수
    view_cnt = soup.select_one('#print_area > div.writerProfile > dl > dt > span > em:nth-child(1)').get_text().strip()

    # 추천수
    like_cnt = soup.select_one('#print_area > div.writerProfile > dl > dt > span > em:nth-child(3)').get_text().strip()

    # 본문 내용
    article = soup.find('div', attrs={'class': 'bodyCont'}).get_text().strip()

    # 댓글 수
    comment_cnt = soup.find('span', attrs={'class': 'comm2'}).get_text().strip()
    new_comment_cnt = str(comment_cnt)[1:-1]

    print(
        '제목: {}\n'.format(title),
        '작성자: {}\n'.format(author),
        '작성일: {}\n'.format(created_at),
        '조휘수: {}\n'.format(view_cnt),
        '추천수: {}\n'.format(like_cnt),
        '본문 내용: {}\n'.format(article),
        '댓글 수: {}\n'.format(new_comment_cnt)
    )

    # 댓글
    comments = []
    comment_all = soup.select('#cmt_reply > li > dl')
    for comment in comment_all:
        comments.append(comment.get_text().strip())
    print(comments)


if __name__ == '__main__':
    url_input = input('보배드림 게시글 url을 입력해 주세요: ')
    main(url_input)