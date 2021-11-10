import scrapWoowa
from datetime import datetime

postLinks = scrapWoowa.postLinks
todayWoowa = []
flagWoowa = False
today = datetime.now().strftime('%b.%d.%Y')
for link in postLinks:
    if today in link[1]:
        flagWoowa = True
        todayWoowa.append(link[0])
