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

    return render_template('index.html',tech_articles=tech_articles,all_articles=all_articles)

@main.route('/kenya')
def kenya():
    kenya_articles = get_article_everything('kenya')

    return render_template('kenya.html',kenya_articles=kenya_articles)