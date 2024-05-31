from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from datetime import datetime
import codecs
from bs4 import BeautifulSoup as b

d = datetime.today()

file_path = f'C:/MyWorkspace/upload/알라딘 베스트셀러 1~400위_{d.year}_{d.month}월_{d.day}.txt'

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴
driver = webdriver.Chrome(options=option, service = service)

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.aladin.co.kr')
t.sleep(2)
 
# driver.find_element(By.XPATH, '//*[@id="Wa_header1_headerTop"]/div[2]/div[3]/ul[1]/li[3]/a').click()
driver.find_element(By.XPATH, '//*[@id="Wa_header1_headerTop"]/div[2]/div[3]/ul[1]/li[3]/a').click()
t.sleep(2)

with codecs.open(file_path, 'w', encoding='utf-8') as f:

  cur_page_num = 2 # 현재 페이지 번호
  target_page_num = 9 # 목적지 페이지 번호
  rank = 1 # 순위

  while cur_page_num <= target_page_num:
    src = driver.page_source

    soup = b(src, 'html.parser')

    div_list = soup.find_all('div', class_='ss_book_box')


    for div in div_list:
      book_info = div.find_all('li')

      if book_info[0].find('span', class_='ss_ht1') == None:
        book_title = book_info[0].text
        book_author = book_info[1].text
        book_price = book_info[2].text
      else:
        book_title = book_info[1].text 
        book_author = book_info[2].text
        book_price = book_info[3].text

      auth_info = book_author.split(' | ')

      f.write(f'# 순위: {rank}위\n')
      f.write(f'# 책 제목: {book_title}\n')
      f.write(f'# 저자: {auth_info[0]}\n')
      f.write(f'# 출판사: {auth_info[1]}\n')
      f.write(f'# 출판일: {auth_info[2]}\n')
      f.write(f'# 가격: {book_price.split(", ")[0]}\n')
      f.write('-'*40)

      rank += 1

    # 다음 페이지로 전환하는 작업
    cur_page_num += 1
    driver.find_element(By.XPATH, f'//*[@id="newbg_body"]/div[3]/ul/li[{cur_page_num}]/a').click()
    del soup   
    t.sleep(2)

    # if cur_page_num == target_page_num:
    #  break
    



