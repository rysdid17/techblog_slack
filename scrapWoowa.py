from bs4 import BeautifulSoup
import requests

# 보고자 하는 곳의 url
blog_woowa = 'https://techblog.woowahan.com/'
# html 텍스트화
html = requests.get(blog_woowa).text
soup = BeautifulSoup(html, 'html.parser')
# html에서 블로그 포스트 링크만 가져오기
linkdata = soup.find_all("div", class_ = "item")
postLinks = []
for link in linkdata:
    postLinks.append((link.find("a").get("href"), link.find("span").text))
