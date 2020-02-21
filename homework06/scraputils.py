import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    tbl_list = parser.table.findAll('table')
    for i in range(30):
        comment = tbl_list[1].findAll('td', {'class': 'subtext'}, 'a')[i].text.split(" | ")[2]
        if not '1' <= comment[0] <= '9':
            com = '0'
        else:
            com = ''
            j = 0
            while '1' <= comment[j] <= '9':
                com = com + comment[j]
                j += 1
        url = tbl_list[1].findAll('a', {'class': 'storylink'})[i].get('href')
        if url[:4] == 'item':
            url = 'https://news.ycombinator.com/' + url
        tmp = {
            'title': tbl_list[1].findAll('a', {'class': 'storylink'})[i].text,
            'author': tbl_list[1].findAll('a', {'class': 'hnuser'})[i].text,
            'points': int(tbl_list[1].findAll('span', {'class': 'score'})[i].text.split()[0]),
            'comments': int(com),
            'url':  url
        }
        news_list.append(tmp)
    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    parser.table.find('a', {'class': 'morelink'}).get('href')
    return parser.table.find('a', {'class': 'morelink'}).get('href')


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news
