'''
We define views that will be rendered on our pages
'''
from flask import render_template,request,redirect,url_for
from . import main
from ..request import *
from .forms import *
from ..models import *

#Views
@main.route('/')
def home():
    tech_articles = get_article_top_headlines('technology')
    all_articles = get_article_everything('all')
    all_sources = get_sources()

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('.search',article=search_article))

    return render_template('index.html',tech_articles=tech_articles,all_articles=all_articles,all_sources=all_sources)

@main.route('/kenya')
def kenya():
    kenya_articles = get_article_everything('kenya')

    return render_template('kenya.html',kenya_articles=kenya_articles)

@main.route('/worldnews')
def worldnews():
    worldnews = get_article_everything('world')

    return render_template('worldnews.html',worldnews=worldnews)

@main.route('/business')
def business():
    business_news = get_article_top_headlines('business')

    return render_template('business.html',business_news=business_news)

@main.route('/sports')
def sports():
    sports_news = get_article_top_headlines('sports')

    return render_template('sports.html',sports_news=sports_news)

@main.route('/health')
def health():
    health_news = get_article_top_headlines('health')

    return render_template('health.html',health_news=health_news)

@main.route('/tech')
def tech():
    tech_news = get_article_top_headlines('technology')

    return render_template('tech.html',tech_news=tech_news)

@main.route('/sources')
def sources():
    all_sources = get_sources()

    return render_template('sources.html',all_sources=all_sources)

@main.route('/search/<article>')
def search(article):
    searched_articles_list = article.split(" ")
    article_name_format = "+".join(searched_articles_list)
    searched_articles = search_article(article_name_format)

    heading = article.upper()
    
    return render_template('search.html',searched_articles=searched_articles,heading=heading)