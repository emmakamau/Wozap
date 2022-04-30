'''
Where we request data from the API e.g
'''

import urllib.request,json
from .models import *

# Getting api key
api_key = None
# Getting the movie base url
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    pass

def get_article(category):
    get_articles_url = base_url.format(category,api_key)
    print(get_articles_url)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results(articles_results_list)

    return articles_results

def process_results(articles_list):
    articles_results = []
    for article in articles_list:
        # author,title,description,url,urlToImage,publishedAt,content
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publisheAt')
        content = article.get('content')
        
        article_object = Article(author,title,description,url,urlToImage,publishedAt,content)
        articles_results.append(article_object)

    return articles_results