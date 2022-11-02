import uglysoup


def main(url):
    soup = uglysoup.get_soup(url)

    # 제목

    # 작성자

    # 작성일

    # 조회수

    # 추천수

    # 본문 내용

    # 댓글 수

    # 댓글


if __name__ == '__main__':
    url_input = 'https://www.bobaedream.co.kr/view?code=best&No=579413&vdate='
    main(url_input)