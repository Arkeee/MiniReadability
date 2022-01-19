## Среда выполнения
Windows

## Описание работы программы:
**Алгоритм получения контента:**
1) Выполняем парсинг по url при помощи библиотек: requests и BeautifulSoup
2) Проверяем подключение к сайту
3) Из страницы достаем все тэги title и p. Производим объединение списка строк.
4) Сохраняем извлеченную информацию в файле.
Примечание: не смог выполнить требование по ограничению количества символов.

## Исходный код программы:
```sh
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
```

## Результаты работы
Для проверки использовалось url:
- https://www.gazeta.ru/politics/news/2022/01/18/17158579.shtml
- https://lenta.ru/news/2022/01/19/go_green/
- https://lenta.ru/news/2022/01/19/mimas/

Результаты работы находятся в папке - "Примеры работы"

## Дальнейшее улучшение/развитие программы.
1. Создание интерфейса
2. Поддержка других тегов, типа 'code', 'article', 'q', 'img'
3. Доработка и оптимизация алгоритма
