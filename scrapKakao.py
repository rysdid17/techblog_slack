from bs4 import BeautifulSoup
import requests

# 보고자 하는 곳의 url
blog_kakao = 'https://tech.kakao.com/blog/'
# html 텍스트화
html = requests.get(blog_kakao).text
soup = BeautifulSoup(html, 'html.parser')
# html에서 블로그 포스트 링크만 가져오기
linkdata = soup.find_all("a", class_ = "link_post")
postLinks = []
# 브런치 주소 등도 섞여 있기 때문에 걸러준다.
for link in linkdata:
    posting = link.get('href')
    if "tech.kakao.com" in posting:
        postLinks.append(posting)
