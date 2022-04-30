'''
We define views that will be rendered on our pages
'''

from flask import render_template,request,redirect,url_for
from . import main
from ..request import *
from .forms import *
from ..models import *

#Views