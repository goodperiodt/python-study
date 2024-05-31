from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
from bs4 import BeautifulSoup as b

# 엑셀 처리 모듈 임포트
# pip install xlsxwriter
import xlsxwriter

# user-agent 정보를 변환해주는 모듈을 import
# 특정 브라우저로 크롤링을 진행할 때 차단되는 것을 방지
# pip install fake_useragent
from fake_useragent import UserAgent

# 이미지를 바이트 단위로 변환 처리 모듈
from io import BytesIO

# 요청 헤더 정보를 꺼내올 수 있는 묘듈
import urllib.request as req



d = datetime.today()

file_path = f'C:/MyWorkspace/upload/알라딘 베스트셀러 1~400위_{d.year}_{d.month}월_{d.day}.xlsx'

# User Agent 정보 변환 (필수는 아니다.)
opener = req.build_opener() # 헤더 정보를 초기화
opener.addheaders = [('User-agent', UserAgent().edge)]
req.install_opener(opener)


# 엑셀 처리 선언
# Workbook 객체를 생성해서 엑셀 파일을 하나 생성 (생성자의 매개값으로는 저장될 경로를 지정
workbook = xlsxwriter.Workbook(file_path)


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
    # div_list = soup.select('div.ss_book_box')


    for div_ss_book_box in div_list:

      # 이미지
      img_url = div_ss_book_box.select_one('table div.cover_area div.flipcover_in > a img.front_cover')
      print(img_url)
      
      # 타이틀, 작가, 가격정보를 모두 포함하는 ul부터 지목
      ul = div_ss_book_box.select_one('div.ss_book_list > ul')

      # 타이틀
      title = ul.select_one('li > a.bo3')

      # 작가
      # 위에서 얻은 title의 부모요소 li의 다음 형제 li를 지목 -> 작가, 출판사, 출판일 존재

      author = title.find_parent().fine_next_sibling()

      # 작가쪽 영역 데이터 상세 분해
      author_data = author.split(' | ')
      author_name = author_data[0].strip()
      company = author_data[1].strip()
      pub_day = author_data[2].strip()

      price = author.find_next_sibling() # 작가 li 다음 형제 요소가 가격 li이다.
      price_data = price.text.split(', ')[0].strip()

      # 책 상세 정보 페이지 링크
      # title이라는 변수에 a 태그를 취득해 놓은 상태
      page_link = title['href']

      try:
        # 이미지 바이트 변환 처리
        img_data = BytesIO(req.urlopen(img_url['src']).read())
        

      except:


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


