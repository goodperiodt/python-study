'''
* 문자열 알파벳 형태 변경 메서드
1. lower(): 영문 알파벳을 모두 소문자로 변경 // toLowerCase()
2. upper(): 영문 알파벳을 모두 대문자로 변경 // toUpperCase()
3. swapcase(): 영문 대소문자를 각각 반대로 변경
4. capitalize(): 문장의 맨 첫글자만 대문자, 나머지는 소문자.
5. title(): 각 단어의 맨 첫글자만 대문자, 나머지는 소문자 (단어는 공백으로 인식)
'''

s = 'GOOD MORning!!! my name is LEE'

print(s)
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.capitalize())
print(s.title())

# swapcase(), capitalize(), title() 은 사용 빈도가 낮은 편