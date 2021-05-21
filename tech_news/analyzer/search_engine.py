from tech_news.database import search_news


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
    """Seu código deve vir aqui"""
#     news_by_date = search_news(
#         {"date": {"$regex": date, "$options": "i"}}
#     )


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
