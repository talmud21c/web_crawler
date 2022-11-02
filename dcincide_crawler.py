import uglysoup


def main(url):
    soup = uglysoup.get_soup(url)

    # ---------------------------본문 내용 출력 테스트-----------------------------------------
    # 글 제목
    article_title = soup.find('span', attrs={'class': 'title_subject'}).get_text().strip()

    #작성자
    nickname = soup.find('span', attrs={'class': 'nickname'}).get_text().strip()

    # 작성자 ip
    ip_address = soup.find('span', attrs={'class': 'ip'}).get_text().strip()

    # 조회 수
    view_cnt = soup.find('span', attrs={'class': 'gall_count'}).get_text().strip()

    # 추천 수
    like_cnt = soup.find('p', attrs={'class': 'up_num'}).get_text().strip()

    # 댓글 수
    comment_cnt = soup.find('span', attrs={'class': 'gall_comment'}).get_text().strip()
    cmt_cnt = comment_cnt.replace('댓글', '')

    # 본문 내용
    content = soup.find('div', attrs={'class': 'write_div'}).get_text().strip()

    # 등록일
    created_at = soup.find('span', attrs={'class': 'gall_date'}).get_text().strip()

    print(
        '제목: {}\n'.format(article_title),
        '작성자: {}\n'.format(nickname),
        '작성자 ip: {}\n'.format(ip_address),
        '작성일: {}\n'.format(created_at),
        '조회수: {}\n'.format(view_cnt),
        '추천수: {}\n'.format(like_cnt),
        '본문 내용: {}\n'.format(content),
        '댓글수: {}\n'.format(int(cmt_cnt))
    )

    # ---------------------------댓글 출력 테스트----------------------------------
    # 일반적인 페이지 요청으로 댓글을 로드하지 못 함.
    # 댓글 요청은 post로 요청
    comments = []
    comment_elements = soup.find_all('li', attrs={'class': 'ub-content'})

    nickname_all = soup.find_all('span', 'nickname')

    comment = soup.find_all('p', attrs={'class': 'ub-word'})

    for element in comment_elements:
        nickname = soup.find('em', attrs={'title': '닉네임'})
        body = element.find('p', attrs={'class': 'ub-word'})
        user_ip = '' if nickname else body.find('span').extract().text
        timestamp = element.find('span', attrs={'class': 'date_time'}).text

        comment = {
            'user_ip': user_ip,
            'nickname': nickname,
            'written_at': timestamp,
            'body': body.text.strip()
        }

        comments.append(comment)


if __name__ == '__main__':
    url_input = input('디시인사이드 게시글 주소를 입력해주세요: ')
    main(url_input)