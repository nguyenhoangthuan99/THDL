import requests
from bs4 import BeautifulSoup
from model.request import RequestSearch
import http3
class BaseService:
    def __init__(self):
        self.client = http3.AsyncClient()
    

    def doQuery(self,url:str):
        htmlText=requests.get(url).text
        soup = BeautifulSoup(htmlText, 'html.parser')
        return soup

    async def asyncDoQuery(self,url):
        htmlText= await self.client.get(url)
        soup = BeautifulSoup(htmlText.text, 'html.parser')
        return soup


    async def process(self,req:RequestSearch):
        raise NotImplementedError
    def rewriteQuery(self,req:RequestSearch)-> str:
        # take request body and rewrite query statement with coresponding web pages
        # return the url of the right webpage
        raise NotImplementedError 

    
        