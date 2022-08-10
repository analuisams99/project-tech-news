from typing import Counter
from tech_news.database import find_news


# Requisito 10
def top_5_news():
    top_news = []
    news_list = find_news()

    sorted_news_list = sorted(
        news_list, key=lambda k: k["comments_count"], reverse=True
    )

    for new in sorted_news_list[:5]:
        top_news.append((new["title"], new["url"]))

    return top_news


# Requisito 11
def top_5_categories():
    top_categories = []
    news_list = find_news()

    for new in news_list:
        top_categories.append(new["category"])

    categories = Counter(sorted(top_categories))
    sorted_categories = sorted(categories, key=categories.get, reverse=True)

    return sorted_categories
