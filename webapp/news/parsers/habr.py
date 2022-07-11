from datetime import datetime

from bs4 import BeautifulSoup

from webapp.news.parsers.utils import get_html, save_news

# def get_news_snippets():
#     html = get_html("https://habr.com/ru/search/?target_type=posts&q=python&order_by=date")
#     if html:
#         soup = BeautifulSoup(html, 'html.parser')
#         all_news = soup.find('ul', class_='content-list_posts').findAll('li', class_='content-list__item_post')
#         for news in all_news:
#             title = news.find('a', class_='post__title_link').text
#             url = news.find('a', class_='post__title_link')['href']
#             published = news.find('span', class_='post__time').text
#             print(title, url, published)



def get_news_snippets():
    html = get_html("https://habr.com/ru/search/?target_type=posts&q=python&order_by=date")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('div', class_='tm-articles-list').findAll('article', class_='tm-articles-list__item')
        for news in all_news:
            title = news.find('a', class_='tm-article-snippet__title-link').text
            url = news.find('a', class_='tm-article-snippet__title-link')['href']
            published = news.find('span', class_='tm-article-snippet__datetime-published').text
            print(title, url, published)