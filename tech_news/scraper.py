import requests
import time
from parsel import Selector
import math
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)

        if response.status_code != 200:
            return None

        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    # print("***************************")
    # print(html_content)
    # print("***************************")
    s = Selector(text=html_content)
    url = s.css("head [rel='canonical'] ").css("link::attr(href)").get()
    title = s.css(".tec--article__header__title::text").get()
    timestamp = s.css("time").xpath("@datetime").get()
    writer = s.css(".tec--author__info__link::text").get()
    if not writer:
        writer = s.css("#js-author-bar > div > p:first-of-type::text").get()
        # #js-author-bar > div > p.z--m-none.z--truncate.z--font-bold
    if not writer:
        writer = s.css("div.tec--timestamp.tec--timestamp--lg > div.tec--timestamp__item.z--font-bold > a::text").get()
    if writer:
        writer = writer.strip()
    shares_element = s.css(".tec--toolbar__item::text").getall()
    shares_count = 0
    if not shares_element:
        shares_count = 0
    else:
        shares_count = shares_element[0].split(" ")[1].split(" ")[0]
        shares_count = int(shares_count)
    comments_element = s.css("#js-comments-btn::text").getall()
    comments_count = 0
    if comments_element:
        comments_element = comments_element[1]
        comments_count = comments_element.split(" ")[1].split(" ")[0]
        comments_count = int(comments_count)
    summary_selector = "div.tec--article__body > p:nth-child(1) *::text"
    summary_content = s.css(summary_selector).getall()
    summary = "".join(summary_content)
    sources = []
    sources_list = s.css(
        ".tec--article__body-grid .z--mb-16 div a::text"
    ).getall()
    for source in sources_list:
        sources.append(source.strip())
    categories = []
    categories_list = s.css("#js-categories a::text").getall()
    for category in categories_list:
        categories.append(category.strip())
    scraped_news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }

    return scraped_news


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    s = Selector(text=html_content)
    part1 = "#js-main > div > div > div.z--col.z--w-2-3 > "
    part2 = "div.tec--list.tec--list--lg > div > "
    part3 = "article > div > h3 > a::attr(href)"
    allLinks = s.css(part1 + part2 + part3).getall()

    if len(allLinks) > 0:
        return allLinks

    return []


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    s = Selector(text=html_content)
    next_page = s.css("div.tec--list.tec--list--lg > a::attr(href)").get()

    if not next_page:
        return None

    return next_page


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    pagination_limit = math.ceil(amount/20)
    url = "https://www.tecmundo.com.br/novidades"
    pages = []
    news = []

    for page_iteration in range(0, pagination_limit):
        response = fetch(url)
        # print(url)
        url = scrape_next_page_link(response)
        pages.extend(scrape_novidades(response))

    # print(pages)

    iteration = 0

    for link in pages:
        response = fetch(link)
        individual_news = scrape_noticia(response)
        # print("*"+ individual_news["writer"] + "*")
        iteration += 1
        # print("*************************")
        # print("*************" + str(iteration) + "************")
        # print("*************************")
        news.append(individual_news)

    result = news[0: amount]
    create_news(result)
    # create_news(news)

    return result


# response = fetch("https://www.tecmundo.com.br/novidades")
# print(response)
# get_tech_news(30)
# get_tech_news(response.text)