import uglysoup


def main(url):
    soup = uglysoup.get_soup(url)

    # ----------본문 내용 크롤링
    article_title = soup.find('span', attrs={'class': 'np_18px_span'}).get_text().strip()

    created_at = soup.find('span', attrs={'class': 'date'}).get_text().strip()

    content = soup.find('div', attrs={'class': 'xe_content'}).get_text().strip()

    nickname = soup.find('a', attrs={'class': 'nick'}).get_text().strip()

    # 조회수, 추천수, 댓글 부분은 class가 없는 b 태그로 작성되어 있어 전체 b태그 검색 후 순서에 따라 추출
    elements = soup.find_all('b')

    # 조회 수
    view_cnt = elements[0].string
    # 추천 수
    recommend_cnt = elements[1].string
    # 댓글 수
    comment_cnt = elements[2].string

    article_data = (article_title, created_at, content, nickname, view_cnt, recommend_cnt, comment_cnt)
    print(article_data)

    # -----------댓글 크롤링
    comments = []
    comment_all = soup.find_all('div', attrs={'class': 'xe_content'})
    for comment in comment_all:
        comments.append(comment.get_text().strip())
    # 배열의 첫 번째 항목이 본문의 내용이므로 삭제
    # del comments[0]
    print(comments)


if __name__ == '__main__':
    url_input = input('에펨코리아 게시글 url을 입력해주세요: ')
    main(url_input)
