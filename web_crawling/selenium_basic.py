# cmd에서 pip install selenium 명령어 작성으로 selenium 패키지 설치하기
# cmd -> pip install selenium (셀레늄 라이브러리 다운로드)

# 셀레늄 라이브러리에서 webdriver를 import 하겠다.
# pip install webdriver_manager
# 파일명은 import하는 라이브러리명과 항상 다르게 작성할 것
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# XPath 등을 통해 요소를 지목하기 위한 클래스
from selenium.webdriver.common.by import By as b
import time as t

# 셀레늄 사용 중 브라우저 꺼짐 현상 방지 옵션
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴
driver = webdriver.Chrome(options=option, service=service)

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.naver.com')

t.sleep(1.5) # 렌더링이 모두 끝난 후 로그인 버튼 요소를 찾기위해 약간의 지연시간을 준다.

# Copy XPath
# 자동으로 버튼이나 링크 클릭 제어하기
# XPath -> XML Path Language
# -> 문서의 특정 요소나 속성에 접근하기 위한 경로로 사용되는 언어
# -> 요소를 중복 없이 정확하게 표현하기 쉬운 언어.

# driver야 XPATH로 요소를 찾아봐(find_element) 
login_btn = driver.find_element(b.XPATH, '//*[@id="account"]/div/a')
login_btn.click()
t.sleep(1)
# 자동으로 텍스트 입력하기
id_input = driver.find_element(b.XPATH, '//*[@id="id"]')
id_input.send_keys('아이디')
t.sleep(1)
driver.find_element(b.XPATH, '//*[@id="pw"]').send_keys('비밀번호')
t.sleep(1)
driver.find_element(b.XPATH, '//*[@id="log.login"]').click()