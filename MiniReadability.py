from bs4 import BeautifulSoup
import requests


class Content:
    def __init__(self, url, title, p):
        self.url = url
        self.title = title
        self.p = p


def get_page(url):
    req = requests.get(url)

    if req.status_code == 200:
        return BeautifulSoup(req.text, 'html.parser')
    return None

def news_from (url):
    bs = get_page(url)
    if bs is None:
        return bs
    titleBs = bs.find("title")
    if titleBs:
        title = titleBs.text
    else:
        title = ' '
    lines = bs.find_all("p")
    p = '\n''\n'.join([line.text.strip() for line in lines])
    return Content(url, title, p)

content = news_from(input('Вставьте ссылку для извлечения информации '))


if content is None:
    print("Ошибка!")
else:
    with open(input('Введите название файла в формате .txt: '), 'w') as f:
        print("Заголовок: {}".format(content.title), file=f)
        print("\nАдрес    : {}\n".format(content.url), file=f)
        print(content.p, file=f)