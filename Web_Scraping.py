# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:37:32 2021

@author: Playdata

Web_Scraping.py : 웹 페이지 읽기 
교재 : 394p

webbrowser : 웹 페이지 접속, open() / open_new() 단, 전달값은 http~~~~
requests   : html 소스 읽기, get() 단, 전달값은 http~~~~
bs4의 BeautifulSoup : html 소스로부터 필요 데이터 검색, 추출
      BeautifulSoup 클래스의 생성자에게 html소스와 'lxml'과 같은 분석 형식을 전달
"""

#### 웹 페이지 접속 모듈 import
import webbrowser

# 접속 URL
url ="http://www.naver.com"

# URL을 통한 웹 접속
webbrowser.open(url)
webbrowser.open_new(url) # 새 창으로 접속(새 탭)


### 검색어를 이용한 웹 접속

## 네이버 기준
# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=파이썬
# 검색주소 : https://search.naver.com/search.naver?
# 검색어 : query=

naver_search_url = 'https://search.naver.com/search.naver?query='
search_word = '파이썬'
webbrowser.open_new(naver_search_url + search_word)


## 구글 기준
# https://www.google.com/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&oq=%ED%8C%8C%EC%9D%B4%EC%8D%AC&aqs=chrome..69i57j0i433i512l2j0i512l7.2291j0j15&sourceid=chrome&ie=UTF-8
# https://www.google.com/search?q=파이썬&oq=파이썬&aqs=chrome..69i57j0i433i512l2j0i512l7.2291j0j15&sourceid=chrome&ie=UTF-8
# 검색주소 : https://www.google.com/search?
# 검색어 : q=파이썬

google_search_url = 'https://www.google.com/search?q='
search_word = "파이썬"
webbrowser.open_new(google_search_url + search_word)


### 동시에 여러 개의 웹 주소로 접속 : 웹 주소들을 리스트에 저장, for문을 이용하여 반복 실행
urls = ['http://www.naver.com', 'http://www.daum.net', 'http://www.google.com']

for url in urls:
    webbrowser.open_new(url)


### 구글에 2개 이싱의 검색어를 전달하여 접속 : 검색어들을 리스트에 저장 후, for 문을 이용하여 반복 실행
google_search_url = 'https://www.google.com/search?q='
search_words = ["python", "python web scraping"]

for word in search_words:
    webbrowser.open_new(google_search_url + word)


#### html 페이지의 소스 요청 : requests 모듈의 get()
import requests

# 대상 페이지의 html 소스 요청 방법 1.
r = requests.get('http://www.naver.com')   
r   # <Response [200]>
r.text[0:100]
# 요청에 대한 응답 페이지 소스는 한줄로 이루어져 있다.


# 대상 페이지의 html 소스 요청 방법 2.
r = requests.get('http://www.naver.com').text
r[0:100]


google_main = requests.get('http://www.google.com')
google_main.text[0:100]


google_main = requests.get('http://www.google.com').text
google_main[0:100]


#### HTML 소스 분석 : bs4 모듈의 BeautifulSoup 클래스
# 모듈 import
from bs4 import BeautifulSoup

# 테스트용 html
html = """
       <html>
       <body>
       <div>
       <span>
       <a href=http://www.naver.com>네이버</a>
       <a href=http://www.daum.net>다음</a>
       <a href=http://www.google.com>구글</a>
       </span>
       </div>
       </body>
       </html>
"""

# BeautifulSoup 객체
soup = BeautifulSoup(html, 'lxml')
'''
<html>
<body>
<div>
<span>
<a href="http://www.naver.com">네이버</a>
<a href="http://www.daum.net">다음</a>
<a href="http://www.google.com">구글</a>
</span>
</div>
</body>
</html>
'''

# 태그명 찾기 : BeautifulSoup 객체.find('검색태그명')
soup.find('a')
'''
<a href="http://www.naver.com">네이버</a>
'''

# 태그명을 검색 후, 시작태그와 닫는태그 사이의 텍스트 추출
soup.find('a').get_text()
'''
'네이버'
'''

# 지정한 모든 태그 검색 : BeautifulSoup 객체.find_all('검색태그명')
soup.find_all('a')
'''
리스트 타입으로 반환
[<a href="http://www.naver.com">네이버</a>,
 <a href="http://www.daum.net">다음</a>,
 <a href="http://www.google.com">구글</a>]
'''

# 지정한 모든 태그 검색 후, 각 태그들의 시작태그와 닫는태그 사이의 텍스트 추출
site_names = soup.find_all('a')
for site_name in site_names:
    print(site_name.get_text())
'''
네이버
다음
구글
'''

## 테스트용 HTML 두번 째
html2 = """
<html>
 <head>
  <title>작품과 작가 모음</title>
 </head>
 <body>
  <h1>책 정보</h1>
  <p id="book_title">토지</p>
  <p id="author">박경리</p>
  
  <p id="book_title">태백산맥</p>
  <p id="author">조정래</p>

  <p id="book_title">감옥으로부터의 사색</p>
  <p id="author">신영복</p>
 </body>
</html>
""" 

# 'lxml' : html 문서를 파싱하기 위한 분석기
soup2 = BeautifulSoup(html2, 'lxml')

# prettify() : html 구조 형태로 정리해서 출력
print(soup2.prettify())

# 태그명을 직접 이용
soup2.title
'''
 <title>작품과 작가 모음</title>
'''

soup2.body
'''
<body>
<h1>책 정보</h1>
<p id="book_title">토지</p>
<p id="author">박경리</p>
<p id="book_title">태백산맥</p>
<p id="author">조정래</p>
<p id="book_title">감옥으로부터의 사색</p>
<p id="author">신영복</p>
</body>
'''

soup2.body.h1
'''
<h1>책 정보</h1>
'''

soup2.find_all('p')
'''
[<p id="book_title">토지</p>,
 <p id="author">박경리</p>,
 <p id="book_title">태백산맥</p>,
 <p id="author">조정래</p>,
 <p id="book_title">감옥으로부터의 사색</p>,
 <p id="author">신영복</p>]
'''

soup2.find('p')
'''
<p id="book_title">토지</p>
'''

soup2.find('p', {'id':'book_title'})
'''
<p id="book_title">토지</p>
'''

soup2.find('p', {'id':'author'})
'''
<p id="author">박경리</p>
'''

soup2.find_all('p', {'id':'book_title'})
'''
[<p id="book_title">토지</p>,
 <p id="book_title">태백산맥</p>,
 <p id="book_title">감옥으로부터의 사색</p>]
'''

soup2.find_all('p', {'id':'author'})
'''
[<p id="author">박경리</p>, <p id="author">조정래</p>, <p id="author">신영복</p>]
'''

book_titles = soup2.find_all('p', {'id':'book_title'})
authors = soup2.find_all('p', {'id':'author'})

for book_title, author in zip(book_titles, authors):
    print(book_title.get_text() + ' : ' + author.get_text())



# BeautifulSoup 객체의 select() 함수를 이용
soup2.select('body h1')
'''
 [<h1>책 정보</h1>]
'''

# select('부모태그명 자식태그명')
soup2.select('body p')
'''
[<p id="book_title">토지</p>,
 <p id="author">박경리</p>,
 <p id="book_title">태백산맥</p>,
 <p id="author">조정래</p>,
 <p id="book_title">감옥으로부터의 사색</p>,
 <p id="author">신영복</p>]
'''

# select('태그명#id명')
soup2.select('p#book_title')
'''
[<p id="book_title">토지</p>,
 <p id="book_title">태백산맥</p>,
 <p id="book_title">감옥으로부터의 사색</p>]
'''


# select('태그명.class명')
"""
만약 태그내에 css 클래스가 있을 경우
<p class=bluecolor>
soup2.select('p.bluecolor')
"""


#### 외부 html을 로드하여 분석 : HTML_example_my_site.html
# Python 기본 함수인 open('읽을 파일의 경로 및 파일', encoding='인코딩방식')
f = open('./data/HTML_example_my_site.html', encoding='utf-8')

# file객체의  read() 를이용하여 읽기
html_source = f.read()

# file 객체 닫기
f.close()

soup3 = BeautifulSoup(html_source, 'lxml')
'''
soup3의 결과
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title>사이트 모음</title>
</head>
<body>
<p id="title"><b>자주 가는 사이트 모음</b></p>
<p id="contents">이곳은 자주 가는 사이트를 모아둔 곳입니다.</p>
<a class="portal" href="http://www.naver.com" id="naver">네이버</a> <br/>
<a class="search" href="https://www.google.com" id="google">구글</a> <br/>
<a class="portal" href="http://www.daum.net" id="daum">다음</a> <br/>
<a class="government" href="http://www.nl.go.kr" id="nl">국립중앙도서관</a>
</body>
</html>
'''


print(soup3.prettify())
'''
<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8"/>
  <title>
   사이트 모음
  </title>
 </head>
 <body>
  <p id="title">
   <b>
    자주 가는 사이트 모음
   </b>
  </p>
  <p id="contents">
   이곳은 자주 가는 사이트를 모아둔 곳입니다.
  </p>
  <a class="portal" href="http://www.naver.com" id="naver">
   네이버
  </a>
  <br/>
  <a class="search" href="https://www.google.com" id="google">
   구글
  </a>
  <br/>
  <a class="portal" href="http://www.daum.net" id="daum">
   다음
  </a>
  <br/>
  <a class="government" href="http://www.nl.go.kr" id="nl">
   국립중앙도서관
  </a>
 </body>
</html>
'''

soup3.select('a.portal')
'''
[<a class="portal" href="http://www.naver.com" id="naver">네이버</a>,
 <a class="portal" href="http://www.daum.net" id="daum">다음</a>]
'''

soup3.select('a#nl')
'''
[<a class="government" href="http://www.nl.go.kr" id="nl">국립중앙도서관</a>]
'''


"""
BeautifulSoup 객체를 이용하여 HTML 소스 분석 방법
1. BeautifulSoup 객체 생성 : BeautifulSoup(html소스, 'lxml')

2. 검색방법
   BeautifulSoup 객체의 find('검색태그명') : 처음 검색된 태그값만 문자열로 반환
   BeautifulSoup 객체의 find_all('검색태그명') : 검색된 모든태그값들을 리스트로 반환
   
   BeautifulSoup 객체의 find('검색태그명', {'id':'id명'}) : 검색된 태그 중 id에 해당하는 처음 값만 문자열로 반환
   BeautifulSoup 객체의 find_all('검색태그명', {'id':'id명'}) : 검색된 태그 중 id에 해당하는 모든 태그값들을 리스트로 반환
   만약 class 값으로 검색할 경우 : {'class':'class명'}
   즉 태그의 속성을 이용하여 검색할 경우 :   {'속성명':'속성값'} 으로 지정하면 된다.
   예) <a href='http://www.naver.com'>네이버</a> 의 경우 : {'href':'http://www.naver.com'}
   
   
   실제 텍스트(시작태그와 닫는태그 사이의 글자)를 추출 : get_text() 
   
   BeautifulSoup 객체.태그명 : 검색된 태그를 문자열로 반환
   BeautifulSoup 객체.상위태그명.하위태그명  : 검색된 태그를 문자열로 반환
   
   BeautifulSoup 객체의 select('태그명')
   BeautifulSoup 객체의 select('상위태그명  하위태그명')
   BeautifulSoup 객체의 select('태그명#id명')
   BeautifulSoup 객체의 select('태그명.class명')
   BeautifulSoup 객체의 select() 는 리스트로 결과값을 반환
"""

#### html 소스의 <br /> 태그를 줄바꿈으로 변경하여 읽어들인 데이터(소스)의 가독성을 높이는 방법 : 변경주체.replace_with(변경값)
# br_example_constitution.html
f = open('./data/br_example_constitution.html', encoding='utf-8')
html_source = f.read()
f.close()

soup4 = BeautifulSoup(html_source, 'lxml')
 
soup4.title

title = soup4.find('p', {'id':'title'})
'''
<p id="title"><b>대한민국헌법</b></p>
'''
print(title.get_text())
'''
대한민국헌법
'''

contents = soup4.find_all('p', {'id':'content'})
'''
[<p id="content">제1조 <br/>①대한민국은 민주공화국이다.<br/>②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.</p>,
 <p id="content">제2조 <br/>①대한민국의 국민이 되는 요건은 법률로 정한다.<br/>②국가는 법률이 정하는 바에 의하여 재외국민을 보호할 의무를 진다.</p>]
'''

for content in contents:
    print(content.get_text())
'''
제1조 ①대한민국은 민주공화국이다.②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.
제2조 ①대한민국의 국민이 되는 요건은 법률로 정한다.②국가는 법률이 정하는 바에 의하여 재외국민을 보호할 의무를 진다.
'''

html = '<p id="content">제1조 <br/>①대한민국은 민주공화국이다.<br/>②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.</p>'

soup5 = BeautifulSoup(html, 'lxml')

br_content = soup5.find('p', {'id':'content'})
'''
<p id="content">제1조 <br/>①대한민국은 민주공화국이다.<br/>②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.</p>
'''

br_content2 = br_content.find('br')
'''
<br/>
'''

br_content2.replace_with('\n')


### 줄 바꿈으로 변경하는 사용자 정의 함수
def replace_newline(soup_html):
    br_to_newlines = soup_html.find_all('br')
    
    for br_to_newline in br_to_newlines:
        br_to_newline.replace_with('\n')
    
    return soup_html


soup6 =BeautifulSoup(html, 'lxml')
content2 = soup6.find('p', {'id':'content'})
content3 = replace_newline(soup6)
print(content3.get_text())
'''
제1조 
①대한민국은 민주공화국이다.
②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.
'''

# html_source : br_example_constitution.html
soup7 = BeautifulSoup(html_source, 'lxml')

title = soup7.find('p', {'id':'title'})
contents =soup7.find_all('p', {'id':'content'})

print(title.get_text(), '\n')
for content in contents:
    content1 = replace_newline(content)
    print(content1.get_text(), '\n')
'''
대한민국헌법 

제1조 
①대한민국은 민주공화국이다.
②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다. 

제2조 
①대한민국의 국민이 되는 요건은 법률로 정한다.
②국가는 법률이 정하는 바에 의하여 재외국민을 보호할 의무를 진다. 
'''


###### 웹 사이트로부터 데이터 가져오기 (순위)
## https://www.alexa.com/topsites/countries/KR

# 1. 해당 웹 사이트 소스 분석을 통해 추출할 데이터 파악
'''
    웹 브라우저를 통해 해당 웹 사이트 접속 후,
    검사(크롬:F12) => elements 탭 선택하여 요소 검색 
'''    

# 2. 요청 URL
url = 'https://www.alexa.com/topsites/countries/KR'

# 3. requests 모듈의 get() 함수를 이용하여 데이터(html 소스) 요청
html_website_ranking = requests.get(url).text

# 4. 데이터(html 소스)를 이용하여 BeautifulSoup 객체 생성
soup_website_ranking = BeautifulSoup(html_website_ranking, 'lxml')

# 5. BeautifulSoup 객체를 이용하여 파악된 데이터에 해당하는 요소 검색
website_ranking = soup_website_ranking.select('p a')
'''
[<a href="https://support.alexa.com/hc/en-us/articles/200444340" target="_blank">this explanation</a>,
 <a href="/siteinfo/google.com">Google.com</a>,
 <a href="/siteinfo/naver.com">Naver.com</a>,
 <a href="/siteinfo/youtube.com">Youtube.com</a>,
 <a href="/siteinfo/daum.net">Daum.net</a>,
 <a href="/siteinfo/tistory.com">Tistory.com</a>,
 <a href="/siteinfo/kakao.com">Kakao.com</a>,
 <a href="/siteinfo/tmall.com">Tmall.com</a>,
 <a href="/siteinfo/coupang.com">Coupang.com</a>,
 <a href="/siteinfo/amazon.com">Amazon.com</a>,
 <a href="/siteinfo/google.co.kr">Google.co.kr</a>,
 <a href="/siteinfo/namu.wiki">Namu.wiki</a>,
 <a href="/siteinfo/netflix.com">Netflix.com</a>,
 <a href="/siteinfo/sohu.com">Sohu.com</a>,
 <a href="/siteinfo/qq.com">Qq.com</a>,
 <a href="/siteinfo/facebook.com">Facebook.com</a>,
 <a href="/siteinfo/wikipedia.org">Wikipedia.org</a>,
 <a href="/siteinfo/taobao.com">Taobao.com</a>,
 <a href="/siteinfo/jd.com">Jd.com</a>,
 <a href="/siteinfo/360.cn">360.cn</a>,
 <a href="/siteinfo/baidu.com">Baidu.com</a>,
 <a href="/siteinfo/microsoft.com">Microsoft.com</a>,
 <a href="/siteinfo/dcinside.com">Dcinside.com</a>,
 <a href="/siteinfo/instagram.com">Instagram.com</a>,
 <a href="/siteinfo/11st.co.kr">11st.co.kr</a>,
 <a href="/siteinfo/yahoo.com">Yahoo.com</a>,
 <a href="/siteinfo/adobe.com">Adobe.com</a>,
 <a href="/siteinfo/office.com">Office.com</a>,
 <a href="/siteinfo/fmkorea.com">Fmkorea.com</a>,
 <a href="/siteinfo/nate.com">Nate.com</a>,
 <a href="/siteinfo/sina.com.cn">Sina.com.cn</a>,
 <a href="/siteinfo/chosun.com">Chosun.com</a>,
 <a href="/siteinfo/twitch.tv">Twitch.tv</a>,
 <a href="/siteinfo/donga.com">Donga.com</a>,
 <a href="/siteinfo/gmarket.co.kr">Gmarket.co.kr</a>,
 <a href="/siteinfo/weibo.com">Weibo.com</a>,
 <a href="/siteinfo/zoom.us">Zoom.us</a>,
 <a href="/siteinfo/apple.com">Apple.com</a>,
 <a href="/siteinfo/danawa.com">Danawa.com</a>,
 <a href="/siteinfo/bing.com">Bing.com</a>,
 <a href="/siteinfo/brunch.co.kr">Brunch.co.kr</a>,
 <a href="/siteinfo/inven.co.kr">Inven.co.kr</a>,
 <a href="/siteinfo/ruliweb.com">Ruliweb.com</a>,
 <a href="/siteinfo/aliexpress.com">Aliexpress.com</a>,
 <a href="/siteinfo/jobkorea.co.kr">Jobkorea.co.kr</a>,
 <a href="/siteinfo/cafe24.com">Cafe24.com</a>,
 <a href="/siteinfo/stackoverflow.com">Stackoverflow.com</a>,
 <a href="/siteinfo/upbit.com">Upbit.com</a>,
 <a href="/siteinfo/google.com.hk">Google.com.hk</a>,
 <a href="/siteinfo/amazon.co.uk">Amazon.co.uk</a>,
 <a href="/siteinfo/auction.co.kr">Auction.co.kr</a>]
'''

website_ranking[0:6]
'''
[<a href="https://support.alexa.com/hc/en-us/articles/200444340" target="_blank">this explanation</a>,
 <a href="/siteinfo/google.com">Google.com</a>,
 <a href="/siteinfo/naver.com">Naver.com</a>,
 <a href="/siteinfo/youtube.com">Youtube.com</a>,
 <a href="/siteinfo/daum.net">Daum.net</a>,
 <a href="/siteinfo/tistory.com">Tistory.com</a>]
'''
website_ranking[0].get_text()
'''
'this explanation'
'''

# 6. 검색결과의 시작태그와 닫는태그 사이의 값만 추출하여 리스트에 저장
website_ranking_address = [ website_ranking_element.get_text()   for website_ranking_element in website_ranking]

website_ranking_address = [ website_ranking_element.get_text()   for website_ranking_element in website_ranking[1:]]

website_ranking_address[0:6]
'''
['Google.com',
 'Naver.com',
 'Youtube.com',
 'Daum.net',
 'Tistory.com',
 'Kakao.com']
'''

print('[Top Sites in South Korea]')
for k in range(6):
    print("{0} : {1}".format(k+1, website_ranking_address[k]))
'''
[Top Sites in South Korea]
1 : Google.com
2 : Naver.com
3 : Youtube.com
4 : Daum.net
5 : Tistory.com
6 : Kakao.com
'''

#### 검색 결과 데이터를 데이터프레임으로...
# 1. 모듈 import
import pandas as pd

# 2. 검색 결과 데이터를 데이터프레임으로 생성하기 위한 dict 생성
website_ranking_dict = {'Website' : website_ranking_address}

# 3. 생성된 dict을 이용하여 데이터프레임 생성
df = pd.DataFrame(website_ranking_dict, 
                  columns=['Website'], 
                  index=range(1, len(website_ranking_address)+1))




##### 벅스 음원 차트 데이터 : https://music.bugs.co.kr/chart/track/week/total?chartdate=20200921
"""
사전 파악 결과

곡명 
select('p.title a')
get_text()


아티스트
select('p.artist a')
get_text()
"""

url = 'https://music.bugs.co.kr/chart/track/week/total?chartdate=20200921'

html_music = requests.get(url).text
soup_music = BeautifulSoup(html_music, 'lxml')

"""
곡명 
select('p.title a')
get_text()
"""
# 곡명 추출 1 : 곡명을 감싸고 있는 태그를 검색하여 저장
titles = soup_music.select('p.title a')
titles[0:3]
'''
[<a adultcheckval="1" aria-label="새창" href="javascript:;" onclick="bugs.wiselog.area('list_tr_09_chart');bugs.music.listen('31999479',true);
 " title="Dynamite">Dynamite</a>,
 <a adultcheckval="1" aria-label="새창" href="javascript:;" onclick="bugs.wiselog.area('list_tr_09_chart');bugs.music.listen('5990595',true);
 " title="Bad Boy">Bad Boy</a>,
 <a adultcheckval="1" aria-label="새창" href="javascript:;" onclick="bugs.wiselog.area('list_tr_09_chart');bugs.music.listen('5956261',true);
 " title="취기를 빌려 (취향저격 그녀 X 산들)">취기를 빌려 (취향저격 그녀 X 산들)</a>]
'''

# 곡명 추출 2 : 검색된 태그들의 텍스트 추출
music_title = [ title.get_text()  for title in titles]
music_title[0:5]
'''
['Dynamite', 'Bad Boy', '취기를 빌려 (취향저격 그녀 X 산들)', 'Tight', '그리워하면 그댈 만날까봐']
'''


"""
아티스트
select('p.artist a')
get_text()
"""
# 아티스트 추출 1 : 아티스트를 감싸고 있는 태그를 검색하여 저장
artists = soup_music.select('p.artist a')
artists[0:2]
'''
[<a href="https://music.bugs.co.kr/artist/80079394?wl_ref=list_tr_10_chart" onclick=" " title="방탄소년단">방탄소년단</a>,
 <a class="artistTitle" href="https://music.bugs.co.kr/artist/80259080?wl_ref=list_tr_10_chart" title="청하">청하</a>]
'''

# 아티스트 추출 2 : 검색된 태그들의 텍스트 추출
music_artist = [ artist.get_text()  for artist in artists]
music_artist[0:5]
'''
['방탄소년단', '청하', '\r\n청하\r\n', '산들', '10CM']
'''

music_artist = [ artist.get_text().strip()  for artist in artists]
music_artist[0:5]
'''
['방탄소년단', '청하', '청하', '산들', '10CM']
'''


##### 날짜(연,월,일)를 입력하면 주간 음악 순위(1~100)의 곡명과 아티스트를 반환하는 사용자 정의 함수
def bugs_music_week_top100(year, month, day):
    
    # 월, 일은 항상 두자리
    month = "{0:02d}".format(month)
    day =  "{0:02d}".format(day)
    
    base_url = 'https://music.bugs.co.kr/chart/track/week/total?'
    url = base_url + 'chartdate={0}{1}{2}'.format(year, month, day)
    
    html_music = requests.get(url).text
    soup_music = BeautifulSoup(html_music, 'lxml')
    
    titles = soup_music.select('p.title a')
    artists = soup_music.select('p.artist a')
    
    music_titles = [title.get_text() for title in titles]
    music_artists = [artist.get_text().strip() for artist in artists]
    
    return music_titles, music_artists

## 날짜를 지정하여 bugs_music_week_top100() 에게 전달
bugs_music_titles, bugs_music_artists = bugs_music_week_top100(2020, 12, 14)


## 파일로 저장
file_name = './data/bugs_top100.txt'

f = open(file_name, 'w')

for k in range(len(bugs_music_titles)):
    f.write("{0:2d} : {1}  /  {2}\n".format(k+1, bugs_music_titles[k], bugs_music_artists[k] ))

f.close()

# 참고 : 파이썬 코드를 이용하여 생성된 파일을 확인할 경우 : glob 모듈의 glob()함수를 이용
import glob

glob.glob(file_name)

## https://www.donga.com/news/search?query=대선



####### 웹 사이트의 이미지를 다운 받아 지정한 폴더에 저장
# https://www.python.org/static/img/python-logo.png
# 하나의 이미지 다운로드
# 1. 이미지의 URL
url = 'https://www.python.org/static/img/python-logo.png'

# 2. requests.get()을 이용하여 이미지 요청 : 
html_image = requests.get(url)

# 3. 이미지 URL중 파일명에 해당하는 부분만 추출하여 저장할 이름으로 사용 : os 모듈 (os.path.basename(url))
import os

image_file_name = os.path.basename(url)
'''
'python-logo.png'
'''

# 4. 저장할 폴더 생성 : os.makedirs('생성폴더명')
#    기존에 폴더가 있는지 여부 : os.path.exists('생성폴더명')  
folder = 'C:/myPyCode/download'

if not os.path.exists(folder):
    os.makedirs(folder)


# 5. 생성된 폴더명과 파일명을 하나로 연결 : os.path.join(폴더명, 파일명)
image_path = os.path.join(folder, image_file_name)
'''
'C:/myPyCode/download\\python-logo.png'
'''

# 6. 이미지 파일을 저장하기 위한 파일 모드 : 'wb'
imageFile = open(image_path, 'wb')

# 7. 이미지 저장 : write(나누어 받아 저장할 바이트수) : byte 단위
chunk_size = 1000000

# 이미지 데이터를 1,000,000 byte 단위로 나누어 파일에 순차적(iter_content(사이즈)으로 저장
for chunk in html_image.iter_content(chunk_size):
    imageFile.write(chunk)

imageFile.close()



#### 여러 개의 이미지를 다운받아 저장
# https://www.reshot.com/search/animal

# 1. 이미지를 다운로드 받을 URL
URL = 'https://www.reshot.com/search/animal'

# 2. 이미지 다운로드 받을 웹 사이트의 HTML 소스 요청
html_reshot_image = requests.get(URL).text

# 3. HTML 소스를 이용하여 BeautifulSoup 객체 생성 : <img src='' > 을 추출하기 위함
soup_reshot_image = BeautifulSoup(html_reshot_image, 'lxml')

# 4. BeautifulSoup 객체를 이용하여 원하는 img 태그 추출
reshot_image_elements = soup_reshot_image.select('a img')
reshot_image_elements[0:3]
'''
[<img alt="Reshot" height="33" src="https://www.reshot.com/build/reshot-logo--mark-cc49363ac3f7876f854286af4266ead51a7ff9e0fa12f30677c9e758d43dd0d1.svg" title="Reshot" width="46"/>,
 ~~~]
'''
# 5. 추출된 img 태그의 src 속성값 추출 : 이미지 데이터를 요청하기 위함
reshot_image_url = reshot_image_elements[1].get('src')
'''
'https://res.cloudinary.com/twenty20/private_images/t_reshot-400/v1521838685/photosp/bae96789-a5ab-4471-b54f-9686ace09e33/bae96789-a5ab-4471-b54f-9686ace09e33.jpg'
'''

# 6. 이미지 URL을 이용하여 이미지 데이터 요청
html_image = requests.get(reshot_image_url)

# 7. 이미지를 저장할 폴더 및 파일명
folder = 'C:/myPyCode/download'

imageFile = open(os.path.join(folder, os.path.basename(reshot_image_url)), 'wb')

chunk_size = 1000000
for chunk in html_image.iter_content(chunk_size):
    imageFile.write(chunk)

imageFile.close()


### URL을 이용하여 이미지 주소를 추출하여 반환하는 사용자 정의 함수
def get_image_url(url):
    html_image_url = requests.get(url).text
    soup_image_url = BeautifulSoup(html_image_url, 'lxml')
    image_elements = soup_image_url.select('a img')
    
    if(image_elements != None):
        image_urls = []
        for image_element in image_elements[1:]:
            image_urls.append(image_element.get('src'))
        return image_urls
    else:
        return None


### 저장 폴더를 지정하여 이미지 주소로부터 이미지를 다운받아 저장하는 사용자 정의 함수
def download_image(img_folder, img_url):
    if(img_url != None):
        html_image = requests.get(img_url)
        
        imageFile = open(os.path.join(img_folder, os.path.basename(img_url)), 'wb')
        
        chunk_size = 1000000
        for chunk in html_image.iter_content(chunk_size):
            imageFile.write(chunk)
            imageFile.close()
    
            print("이미지 파일명 : '{0}'. 내려받기 완료".format(os.path.basename(img_url)))
    else:
        print("내려받을 이미지가 없습니다.")

# 이미지 다운 사이트 URL
reshot_url = 'https://www.reshot.com/search/animal'

# 사용자 정의 함수를 이용한 이미지 주소 가져오기
figure_folder = 'C:/myPyCode/download'

reshot_image_urls = get_image_url(reshot_url)

num_of_daownload_image =7
for k in range(num_of_daownload_image):
    download_image(figure_folder, reshot_image_urls[k])

print("선택한 이미지 내려받기 종료")



"""
Python 팀 프로젝트 명단 
(명단은 가나다순으로 입력되어 있습니다)					
1 조	강재균	김기환	이성찬	정훈오	
2 조	권기철	김치우	서두현	조용기	주현준
3 조	신우주	이예지	이형걸	전재연
4 조	김지영	남지희	정광수	정치영	
"""









