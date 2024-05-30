# 1. selenium 모듈? 라이브러리? 패키지? 에서 webdriver를 import하겠다.
# 2. webdriver가 초기화되면 webdriver_manager가 만들어지는 것 같다. 그리고 webdriver_manager가 갖는 chrome에서 ChromeDriverManager를 import하는 것 같다.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from bs4 import BeautifulSoup as b


# selenium 사용중 브라우저 꺼짐 현상 방지 옵션
# 프로그램이 끝나도 selenium으로 열린? 브라우저는 계속 켜져있게 하기

# option = webdriver.ChromeOptions()
# option.add_experimental_option

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴
driver = webdriver.Chrome(options=option, service = service)

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.aladin.co.kr')
t.sleep(2)
driver.find_element(By.XPATH, '//*[@id="Wa_header1_headerTop"]/div[2]/div[3]/ul[1]/li[3]/a').click()
t.sleep(2)

# selenium으로 현재 페이지의 html 소스 코드를 전부 불러오기
src = driver.page_source
# print(type(src)) <class 'str'>
# 문자열을 html 문법으로 변환하는 명령어

# soup이란 변수에 html문법에 맞게 변환된 소스코드가 담겨있다.
soup = b(src, 'html.parser')

# html문서에서 div태그이면서 class명이 ss_book_box인 요소를 전부 추출하여 리스트에 담아 대입한다.
div_list = soup.find_all('div', class_='ss_book_box')

# print('div_list에 들어있는 데이터의 수: ', len(div_list))
# print(div_list[0]) # 1위 책만 한번 출력해봄
first_book = div_list[0].find_all('li')

book_title = first_book[1].text
# print(book_title) [국내도서] 선재 업고 튀어 1~2 세트 - 전2권 - 이시은 작가, 변우석·김혜윤·송건희·이승협 배우 사인, 메시지 수록, 양장
book_author = first_book[2].text 
# print(book_author) 이시은 (지은이) | 북로그컴퍼니 | 2024년 7월
book_price = first_book[3].text

auth_info = book_author.split(' | ')
# print(auth_info) 문자열에서 | 를 기준으로 잘라서 배열로 전달받아 출력하면
# 결과는 다음과 같다. ['이시은 (지은이) ', ' 북로그컴퍼니 ', ' 2024년 7월']

print(f'제목: {book_title}')
print(f'저자: {auth_info[0]}')
print(f'출판사: {auth_info[1]}')


print(f'출판일: {auth_info[2]}')
# print(book_price)
print(f'가격: {book_price.split(", ")[0]}')

