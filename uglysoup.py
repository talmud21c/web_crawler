import requests
from bs4 import BeautifulSoup


def get_soup(url):
    webpage_url = url

    session = requests.Session()
    session.get(url)

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    webpage = requests.get(webpage_url, headers=headers)

    soup = BeautifulSoup(webpage.content, 'lxml')

    return soup
