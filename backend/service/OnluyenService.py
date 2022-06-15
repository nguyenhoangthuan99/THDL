from .Base import BaseService
from model.request import RequestSearch
from model.responses import Response
import asyncio
from fastapi import HTTPException

class OnluyenService(BaseService):
    def __init__(self):
        super(OnluyenService,self).__init__()

    def rewriteQuery(self, req: RequestSearch) -> str:
        url = None
        if req.grade == None or grade < 6:
            return url
        else: 
            grade = str(req.grade)
            if req.subject == "MATH":
                url = f"https://www.onluyen.vn/thu-vien-tai-lieu/toan-{grade}/" 
            if req.subject == "PHYSIC":
                url = f"https://www.onluyen.vn/thu-vien-tai-lieu/vat-ly-{grade}/"
            if req.subject == "CHEMISTRY":
                if req.grade < 8:
                    url = None
                    return url
                else:
                    url = f"https://www.onluyen.vn/thu-vien-tai-lieu/hoa-{grade}/"
            if req.subject == "BIOLOGY":
                url = f"https://www.onluyen.vn/thu-vien-tai-lieu/sinh-{grade}/"
        
        if req.page > 1 and url != None:
            url += "page/" +str(req.page)
        return url
    
    def parser_html(self,soup):
        results = []
        try:
            records = soup.find_all('div', class_='entry-item')
            for record in records:
                date = None
                content = record.find('h5',class_='entry-title').find("a")
                title = content.get("title")
                link = content.get("href")
                result = Response(title=title,link=link,date=date,source="onluyen").dict()
                results.append(result)
            return results
        except Exception as e:
            print(e)
            return results

    async def process(self,req:RequestSearch):
        results = []
        if req.text is None or req.text == "":
            
            url = self.rewriteQuery(req)
            print(url)
            if url == None:
                return results
            soup = await self.asyncDoQuery(url)
        
            if soup == None:
                raise HTTPException(404,"Not found, try again later")
            results = self.parser_html(soup)
            print(results)
            return results
        else:
            candidates = []
            page = req.page
            list_soup = []
            for i in range((page-1)*5,page*5):
                if i == 0 :continue
                req.page=i
                url = self.rewriteQuery(req)
                if url == None:
                    continue
                fut = self.asyncDoQuery(url)
                list_soup.append(fut)
            temps = await asyncio.gather(*list_soup)
            
            for temp in temps:
                
                if temp == None: continue
                else:
                    candidates.append(temp)
            for x in candidates:
                #print(type(x))
                results+=self.parser_html(x)
           # candidates = [ for x in candidates]
            results = self.filterQuery(req.text,results)
            
            return results