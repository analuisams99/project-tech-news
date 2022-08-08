import time
import requests

from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )

        time.sleep(1)

        if response.status_code == 200:
            return response.text
        else:
            return None

    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css("div.cs-overlay a ::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css("div.nav-links a.next ::attr(href)").get()

    if next_page_url:
        return next_page_url
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = selector.css("link[rel='canonical'] ::attr(href)").get()
    title = (
        selector.css("div.entry-header-inner h1.entry-title ::text")
        .get()
        .strip()
    )
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("li.meta-author span.author a ::text").get()
    comments_count = len(selector.css("ol.comment-list").getall())
    summary = "".join(
        selector.css("div.entry-content > p:nth-of-type(1) *::text").getall()
    ).strip()
    tags = selector.css(".post-tags ul li a ::text").getall()
    category = selector.css("a.category-style span.label ::text").get()

    news_information_dict = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }

    return news_information_dict


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
