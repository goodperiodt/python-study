'''
* 문자열 분할 *

- split() 메서드는 구분자를 기준으로 문자열을 분할해서
리스트에 담아서 반환됩니다. 

'''

s1 = '떡볶이 김말이 닭강정'
print(s1.split()) # 파이썬은 ()괄호 안에 매개값을 전달하지 않으면 공백을 구분자로 하여 분할한다.

s2= '홍길동 | 대한출판사 | 2024년 05월'
data = s2.split(' | ') # 앞 뒤에 공백있고, | 기호를 구분자로 문자열을 분할해줘

print('저자: ', data[0])
print('출판사: ', data[1])
print('출판년월: ', data[2])