'''
* 파일 입/출력
- 프로그램이 생성한 정보를 좀 더 오래 저장할 때는
파일에 기억해야 합니다.
- 메모리는 속도는 빠르지만 전원이 끊어지면 정보를 잃어버릴 수
있기 때문에, 하드디스크에 저장해야 데이터를 오래 보관할 수
있습니다.
- 파일은 정보를 저장하는 기본 단위이며
문서, 이미지, 멀티미디어 자료도 모두 파일 형태로 보관할 수
있습니다.
- 파이썬에서는 파일 입/출력을 할 때
open()이라는 함수를 사용합니다.
ex) open('파일 경로', 모드)
- 파일 경로는 입/출력 대상의 파일 경로입니다.
디렉터리 경로를 포함시킵니다.
- 모드는 읽기, 쓰기, 추가 등 무엇을 할 지
결정하는 인수입니다.
- 모드의 종류
1. r: 파일을 읽어들입니다. 읽어들일 파일이 없으면
예외가 발생합니다.
2. w: 파일에 데이터를 저장합니다.
파일이 이미 존재한다면 덮어씁니다.
3. a: 파일에 데이터를 추가합니다. (이미 존재하는 파일에)
파일이 존재하지 않는다면 새롭게 생성도 해 줍니다.
'''

# 파일 입출력은 외부 데이터로 접근하기 때문에
# 예외처리를 통해 안전하게 작성하는 것을 권장합니다.

try:
  # 파일 저장 가능 (write, append)
  file_path = r'C:\MyWorkspace\upload\test2.txt'
  # 파일 입출력을 실행하는 내장 함수 open()
  # 반환 값으로 파일 입출력을 담당하는 객체가 리턴됩니다.
  # 첫 번째 인수로 파일 경로를, 두번째 인수로 모드(읽어들일 건지, 쓸건지)를 설정
  # 모드를 'w'로 설정시, 기존에 존재하는 파일명에 내용을 쓸시, 기존의 내용은 삭제되고, 새로운 내용이 작성된다.
  # 만약 기존 내용에 내용을 덧붙이고 싶다면 모드를 'a'로 할 것
  # a 모드는 기존의 내용에 추가할 때 사용하는 모드인데, 만약 파일이 없다면
  # 파일을 새롭게 생성해준다.
  f = open(file_path, 'a')


  text = """바꿈 바꿈
  """

  # 파일을 저장할 때는 write() 메서드 사용
  # 저장할 데이터를 인수로 전달합니다.
  f.write(text)
  print('저장 완료')

except: # 에러발생시 하기 실행문 수행
  print('파일 저장 실패!')

finally:
  # 예외 발생 여부와 상관 없이 항상 실행되는 문장을 작성한다.
  # 파일 입출력은 하드디스크 자원을 사용하는 코드이므로
  # 반드시 사용 후 그 자원을 해제하여 메모리 누수를 방지한다.
  f.close()