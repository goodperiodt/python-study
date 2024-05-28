'''
* 내장함수 range()
- 순차적으로 증가하는 정수의 순차적 자료형을 만들 때
대괄호 안에 데이터들을 콤마로 일일히 나열하는 것은
한계가 있기 때문에, range()함수를 통해 보다 쉽게
순차형 반복 범위를 지정할 수 있습니다.
ex) range(begin, end, step)
- begin은 값이 포함되지만(이상), end는 값이 포함되지 않습니다. (미만)
'''

total = 0
for n in range(1, 101, 1):
    total += n

print('total: ', total)


list1 = [1,2,3,4,5,6,7,8,9,10]
for n in list1:
    print(n, end='  ')

print()

for n in range(1, 11, 1):
    print(n, end='  ')

print()

for n in range(4, 15): # step을 작성하지 않을 시(step 생략시) step의 값은 1로 처리된다.
    print(n, end='  ')

print()

for n in range(5): # range()의 매개 변수로 하나의 값을 준다면,
    # 전달된 하나의 매개 변수는 end 값에 대입된다.
    # start값은 0, step의 값은 자동으로 1로 처리된다.
    # range(5) 는 range(0, 5, 1) 과 같다.

    ## range 함수 괄호 안에 값을 한 개만 주면 end로 처리하고,
    ## begin값을 자동으로 0으로 처리한다.
    print(n, end='  ')


total = 0
for n in range(1, 10001): # 1부터 10000까지의 누적 합계를 구할 때
    total += n

print('total: ', total)



