from .Base import BaseService
from model.request import RequestSearch
from model.responses import Response


class ToanMathService(BaseService):
    def __init__(self,):
        super(ToanMathService, self).__init__()
        

    def rewriteQuery(self,req:RequestSearch)-> str:
        url = None
        if req.level == "3" and req.subject == "MATH":
            if req.type == "TRY":
                url = "https://toanmath.com/de-thi-thu-mon-toan"
            elif req.type in ["MidHK1","MidHK2","HK1","HK2"]:
                if req.type in ["MidHK1","MidHK2"]:
                    phase = "-giua"
                else:
                    phase = ""
                url = f"https://toanmath.com/de-thi{phase}-hk1-toan-{req.grade}"
            elif req.type == "HSG":
                url = f"https://toanmath.com/de-thi-hsg-toan-{req.grade}" 
        if req.page > 1 and url != None:
            url += "/page/"+str(req.page)
        return url

    async def process(self,req:RequestSearch):
        if req.text is None or req.text == "":
            results = []
            url = self.rewriteQuery(req)
            soup = await self.asyncDoQuery(url)
            records = soup.find_all('div', class_='mh-col-1-2 mh-posts-grid-col clearfix')
            for record in records:
                date = record.find("div",class_='mh-meta entry-meta').find("a")
                #print(date)
                date = date.contents[0]
                content = record.find('h3',class_='entry-title mh-posts-grid-title').find("a")
                title = content.get("title")
                link = content.get("href")
                result = Response(title=title,link=link,date=date).dict()
                results.append(result)
            return results
        else:

            return []