import requests
from bs4 import BeautifulSoup
from model.request import RequestSearch
class BaseService:
    def __init__(self):
        pass
    def downloadHTML(self,url:str):
        res = requests.get(url).text
        return res

    def initSoup(self,htmlText:str):
        soup = BeautifulSoup(htmlText, 'html.parser')
        return soup

    def doQuery(self,url):
        return self.initSoup(self.downloadHTML(url))

        
    def process(self,req:RequestSearch):
        raise NotImplementedError
    def rewriteQuery(self,req:RequestSearch)-> str:
        # take request body and rewrite query statement with coresponding web pages
        # return the url of the right webpage
        raise NotImplementedError 

    
        