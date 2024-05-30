'''
* 키워드 인수 (keyword argument)
- 인수의 개수가 많아지면 인수의 순서를 파악하기 어렵고
함수를 호출할 때 전달할 값의 위치를 헷갈릴 가능성이
높아집니다.
ex) def signup_user(id, pw, name, addr, email, phone .....)
- 파이썬에서는 순서와 무관하게 인수를 전달할 수 있는
방법을 제공하여 인수의 이름을 직접 지정하여 값을 전달하는
키워드 인수 방식을 제공합니다.
'''

def calc_sum(begin, end, step):
  sum = 0
  for n in range(begin, end+1, step):
    sum += n
  return sum

# 일반적인 함수 호출 (위치 인수 -> positional argument)
calc_sum(3, 7, 1)

# 키워드 인수 사용 (순서 상관 x)
# 함수 선언시 작성한 파라미터의 순서와 상관 없이
# 지목해서 직접 매개변수에 인수를 전달한다면 함수의 실행에 문제 없다.
print(calc_sum(end=7, begin=3, step=1))
print(calc_sum(step=1, begin=3, end=7))

# 위치 인수와 키워드 인수의 혼합 사용시에는
# 무조건 위치 인수가 앞에 와야 한다.
print(calc_sum(3, step=1, end=7)) # 여기서 3은 begin파라미터에 전달된다.
# print(calc_sum(3, 1, end=7)) (x)
# print(calc_sum(end=7, 3, 1)) (x) SyntaxError: 키워드 인수가 앞에 쓰여 에러가 발생한다.
# print(calc_sum(3, end=7, 1)) (x) SyntaxError : 키워드 인수(end=7)가 위치 인수(1)보다
# 앞에 쓰이면 무조건 구문 에러가 발생한다.

# 위치 인수와 키워드 인수의 혼합 사용 예제
print(3, 6, 9, sep='->', end='!')

