import scrapKakao
from datetime import datetime

postLinks = scrapKakao.postLinks
todayPost = []
flagKakao = False
today = datetime.now().strftime('%Y/%m/%d')
for link in postLinks:
    if today in link:
        flagKakao = True
        todayPost.append(link)
