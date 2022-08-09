from datetime import datetime
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
    try:
        news_found = []
        date_format = "%Y-%m-%d"
        db_date = "%d/%m/%Y"

        parse = datetime.strptime(date, date_format)

        for news in search_news({"timestamp": parse.strftime(db_date)}):
            news_found.append((news["title"], news["url"]))

        return news_found

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
