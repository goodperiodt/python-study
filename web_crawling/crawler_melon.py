from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from datetime import datetime
import codecs
from bs4 import BeautifulSoup as b

# 오늘 날짜 얻어오기
d = datetime.today()

file_path = f'C:/MyWorkspace/upload/멜론차트 1~100위_{d.year}_{d.month}_{d.day}.txt'

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

service = webdriver.ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(options=option, service = service)

driver.get('https://www.melon.com/index.htm')
t.sleep(2)

driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]').click()
t.sleep(2)

# 순위 곡정보 앨범 

with codecs.open(file_path, 'w', encoding='utf-8') as f:

  # 현재 페이지의 소스 코드 얻어와서 src 변수에 담기
  src = driver.page_source
  # 얻어온 소스코드 html문법에 맞게 변환하고 soup 변수에 담기
  soup = b(src, 'html.parser')

  # html문법에 맞게 변환된 소스코드에서 태그가 tr이고, 클래스명이 lst50인 태그들의 리스트를 반환한다.

  for cnt in [50, 100]:
    # 곡 정보가 있는 tr 리스트를 지목해서 얻어오자 (lst50, lst100으로 나누어져 있음)
    song_tr_list = soup.select(f'.lst{cnt}')


    for song_tr in song_tr_list:
      # 공백이 존재할 수 있으니 strip()을 작성해준다.
      rank = song_tr.select_one('div.wrap.t_center').text.strip()
      print(rank)

      # 가수 이름 찾기
      artist_name = song_tr.select_one('div.wrap div.ellipsis.rank02 > a').text.strip()
      print(artist_name)

      # 앨범명 찾기
      album_name = song_tr.select_one('div.wrap div.ellipsis.rank03 > a').text.strip()
      print(album_name)

      # 노래명 찾기
      song_name = song_tr.select_one('div.wrap div.ellipsis.rank01 > span > a').text.strip()
      print(song_name)

      print('-'*40)
      f.write(f'# 순위: {rank} \n')
      f.write(f'# 가수명: {artist_name} \n')
      f.write(f'# 앨범명: {album_name} \n')
      f.write(f'# 노래 제목: {song_name} \n')




    






