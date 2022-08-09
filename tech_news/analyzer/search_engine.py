from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news_found = []
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})

    for news in news_list:
        news_found.append((news["title"], news["url"]))

    return news_found


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
