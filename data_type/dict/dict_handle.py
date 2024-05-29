'''

* 사전 내부 데이터 관리
- 사전은 변경 가능한 자료형이어서 실행 중에 데이터의
추가, 삭제, 수정 등의 편집을 자유롭게 진행할 수 있습니다.

'''

# 데이터 추가하기
# 사전 내부에 존재하지 않는 키(key)를 사용하여 데이터를 대입하면
# 데이터가 key:value 쌍으로 사전에 저장됩니다.

eng_kor = {'student':'학생', 'apple':'사과', 'book':'책'}
eng_kor['banana'] = '바나나' # dict 타입 객체를 참조하고 있는
# 기존의 dict 타입 객체내부에 없는 키를 갖고, 참조변수명['key'] = 'value'
# 를 한다면 dict 타입 객체에 'key' : 'value' 형식으로 데이터가 추가 된다.

# 사전에 데이터를 수정하기
# 사전 내부에 이미 존재하는 key를 사용하여 새로운 데이터를
# 대입하면 해당 key 값에 매핑되어 있는 value가 수정된다.
eng_kor['book'] = '서적'
print(eng_kor)

'''
사전의 key 목록과 value 목록을 따로따로 추출하고 싶다면
사전의 keys(), values()를 사용합니다.

'''

print('-'*40)
print(eng_kor.keys()) # dict_keys(['student', 'apple', 'book', 'banana'])
print(eng_kor.values()) # dict_values(['학생', '사과', '서적', '바나나'])

# 사전의 반복문 처리
# for ~ in 뒤에 사전 데이터를 적으면 key만 반복 순회한다.
for c in eng_kor: # for c in eng_kor.keys():
  print(c)

'''
* 사전의 데이터 삭제 (내장함수 del을 사용)
del(사전이름[key])
key를 전달하면 같이 맵핑된 value도 함께 삭제된다.
'''

del eng_kor['student']
print(eng_kor) # student(key)와 매핑된 '학생'(value) 데이터도 함께 삭제된다.

# 빈 사전 만들기
d = {}
d2 = dict()
print(d, d2)