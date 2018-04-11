from django.shortcuts import render
from django.utils import timezone
from .models import Post

import csv, numpy as np, scipy as sp, matplotlib.pyplot as plt, pandas as pd, json as js, collections as cl, ast, IPython.display as ip, mpld3
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Create your views here.
df1 = pd.read_csv('blog\crypto-markets.csv')

def post_list(request):
    posts = Post.objects.order_by('published_date')
    
    graph1 = graphOverall()
    graph2 = graphEthereum()
    graph3 = graphRipple()
    graph4 = graphUSD()
    return render(request, 'blog/post_list.html', {'posts': posts,'graph1': graph1, 'graph2': graph2, 'graph3': graph3, 'graph4':graph4})



def graphOverall():
    fig = Figure()
    ax = fig.add_subplot(111)
    
    ax.set_xlabel("Market cap")
    ax.set_title("Top 10 Currencies by Market Cap")
    x = df1.groupby(['name'])['market'].last().sort_values(ascending=False).head(10).sort_values()
    x.plot(ax=ax,kind='bar')
    
    canvas = FigureCanvas(fig)
    g = mpld3.fig_to_html(fig)
    return g

def graphEthereum():
    fig = Figure()
    ax = fig.add_subplot(111)
    
    dfEFull = df1.loc[df1['name'] == 'Ethereum']
    dfE = dfEFull['market']
    y = dfE
    x = dfEFull['date']
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    ax.set_title("Ethereum")
    ax.plot(x, y, marker = "o", linestyle='None', color = 'purple')
    
    canvas = FigureCanvas(fig)
    g = mpld3.fig_to_html(fig)
    return g

def graphRipple():
    fig = Figure()
    ax = fig.add_subplot(111)
    
    dfEFull = df1.loc[df1['name'] == 'Ripple']
    dfE = dfEFull['market']
    y = dfE
    x = dfEFull['date']
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    ax.set_title("Ripple")
    ax.plot(x, y, marker = "o", linestyle='None', color = 'blue')
    
    canvas = FigureCanvas(fig)
    g = mpld3.fig_to_html(fig)
    return g

def graphUSD():
    fig = Figure()
    ax = fig.add_subplot(111)
    
    dfUSAFull = pd.read_csv('blog\DTWEXB.csv', na_values='.')
    dfUSA = dfUSAFull['VALUE']
    y = dfUSA
    x = dfUSAFull['DATE']
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    ax.set_title("Trade Weighted U.S. Dollar Index")
    ax.plot(x, y, marker = "o", linestyle='None', color = 'blue')
    
    canvas = FigureCanvas(fig)
    g = mpld3.fig_to_html(fig)
    return g
