from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    title_list_news = search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    tuple_list = []
    for title_news in title_list_news:
        tuple_list.append((title_news["title"], title_news["url"]))
    return tuple_list


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        news_by_date = search_news(
            {"timestamp": {"$regex": date}}
        )
        list_news = []
        for news in news_by_date:
            list_news.append((news["title"], news["url"]))
        return list_news
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_source(source):
    news_by_source = search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )
    list_news = []
    for news in news_by_source:
        list_news.append((news["title"], news["url"]))
    return list_news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
