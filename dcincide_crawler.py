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

    # 댓글 수
    comment_cnt = soup.find('span', attrs={'class': 'gall_comment'}).get_text().strip()
    cmt_cnt = comment_cnt.replace('댓글', '')
    print(int(cmt_cnt))

    # 본문 내용
    content_all = soup.find('div', attrs={'class': 'writing_view_box'})
    content = content_all.p.get_text().strip()

    # 등록일
    created_at = soup.find('span', attrs={'class': 'gall_date'}).get_text().strip()

    article_data = (article_title, nickname, ip_address, view_cnt, comment_cnt, content, created_at)
    print(article_data)

    # ---------------------------댓글 출력 테스트----------------------------------
    # 일반적인 페이지 요청으로 댓글을 로드하지 못 함.
    # 댓글 요청은 post로 요청
    comments = []
    comment_elements = soup.find_all('li', attrs={'class': 'ub-content'})
    print(comment_elements)

    nickname_all = soup.find_all('span', 'nickname')
    print(nickname_all)

    comment = soup.find_all('p', attrs={'class': 'ub-word'})
    print(comment)

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

    print(comments)


if __name__ == '__main__':
    url_input = input('디시인사이드 게시글 주소를 입력해주세요: ')
    main(url_input)