# module 내에 존재하는 변수, 함수, 클래스 등을 직접 import하는 방법

from math import factorial, gcd
# import할 모듈의 별칭을 지정하여 사용하기
import statistics as st

print(factorial(10))
print(gcd(12, 18)) # 12와 18의 최대공약수를 구하는 math라는 묘듈의 gcd()

li = [34, 55, 12, 33, 55, 66, 99]
# print(f'평균은 {statistics.mean(li)}')
# print(f'분산: {statistics.variance(li)}')
print(f'평균은 {st.mean(li)}')
print(f'분산: {st.variance(li)}')

# 위에서 배운 두 가지 개념을 합쳐서도 사용이 가능하다.
from math import factorial as fac

print(fac(8))