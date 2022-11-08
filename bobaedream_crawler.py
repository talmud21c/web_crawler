import uglysoup
import csv


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

    # test text density
    div = soup.find('div', {'class': 'content02'})
    children = div.findChildren()

    text_density = len(article)/len(children)

    print('Text Density for <div class:content02> is {}'.format(text_density))

    # filename = title
    # f = open(filename, 'w', encoding='utf-8-sig', newline='')
    #
    # try:
    #     writer = csv.writer(f)
    #     writer.writerow(('제목', '작성자', '작성일', '조회수', '추천수', '본문 내용', '댓글 수'))
    #     writer.writerow((title, author, created_at, view_cnt, like_cnt, article, new_comment_cnt))
    # finally:
    #     f.close()

    print(
        '제목: {}\n'.format(title),
        '작성자: {}\n'.format(author),
        '작성일: {}\n'.format(created_at),
        '조회수: {}\n'.format(view_cnt),
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