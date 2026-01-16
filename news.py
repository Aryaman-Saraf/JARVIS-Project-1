import requests

from newsapi import NewsApiClient


newsapi = NewsApiClient(api_key='e2a7e34fa62b404c8a8068833f12e29a')
def topHeadLines():
        top_headlines = newsapi.get_top_headlines(#q='bitcoin',
                                                
                                                #category='',
                                                language='en',
                                                country='us')
        sources = newsapi.get_sources()
        print(top_headlines)

topHeadLines()

#In development phase
