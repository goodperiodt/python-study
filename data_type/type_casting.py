name = '홍길동'
score = 90

print(name + '의 점수는 ' + str(score) + '점 입니다.')

# 숫자로 이루어진 문자열을 정수로 변환할 때는 int()를 사용
n1 = 10
n2 = '34'
print(n1 + int(n2))

# 실수로 이루어진 문자열을 실수로 변환할 때는 float()를 사용.
s = '2.34'
print(10 + float(s))
print(10 + float('3.14e-2'))

# 반올림을 할 때는 round() 함수를 사용합니다.
print('-' * 30)

print(round(4.78))

# 반올림할 자리수를 선택하려면 함수의 두번째 매개값으로 자리수를 지정.
print(round(4.78, 1))