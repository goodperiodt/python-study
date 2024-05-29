# dictionary data-type은 자바의 map을 생각하면 된다.

'''
* 사전 (Dictionary)
- 사전은 키(key)와 값(value)의 쌍을 저장하는 대용량의 자료구조.
- 사전은 타 언어에서는 Map이라고도 부르며 연관배열이라고도 부릅니다.
- 사전을 정의하는 기호는 {}이고, 괄호 안에 데이터를 
key : value 형태로 나열하여 저장합니다.
'''

students = {'멍멍이':'홍길동', '야옹이':'박영희', '떽떽이':'김철수'}

print(type(students)) # <class 'dict'>
print(len(students)) # 3, 하나의 쌍은 key : value 로 맵핑이된

'''
- 사전에 사용되는 key값은 중복값을 가질 수 없고, 변경도 안됩니다.
- 반면에 value값은 중복을 허용하고, 데이터를 자유롭게 편집할 수도
있습니다.
- 사전 내부에 저장된 데이터를 검색할 때는 인덱스 대신
key를 사용합니다. (시퀀스 자료형이 아닙니다.)

'''

print(students['멍멍이']) # key를 지목하면 value가 나온다.
# 자바에서는 map.get()
print(students['야옹이'])
print(students['떽떽이'])
# print(students['메뚜기']) (x) 없는 키 값을 주면 에러가 남 

print('멍멍이' in students)
print('야옹이' in students)
print('떽떽이' in students)
print('메뚜기' in students) # False

key = '멍멍이'
if key in students:
  print(students[key])
else:
  print(f'{key}를 별명으로 갖는 사람은 없습니다.')

