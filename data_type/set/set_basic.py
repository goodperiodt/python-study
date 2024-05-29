'''
* 집합 (set)
- 집합은 여러 값들의 모임이며, 저장 순서가 보장되지 않고
 중복값의 저장을 허용하지 않습니다.
- 집합은 사전과 마찬가지로 {}로 표현하지만, key:value
쌍이 아닌, 데이터가 하나씩 들어간다는 점이 사전과는 다릅니다.
- set()함수는 공집합을 만들기도 하며, 다른 컬렉션 자료형을
집합 형태로 변환할 수도 있습니다.
# []-list(), tuple(), {}-dict(), set()
'''


names = {'홍길동', '김철수', '박영희', '고길동', '홍길동'}
print(type(names)) # <class 'set'> {} 중괄호로 선언했음에도
# key:value 의 형태가 아니라 set으로 인식

print(names)

for x in names:
  if x == '김철수':
    print(x)
    break

# 내장함수 set()
s = set()
print(type(s))
print(s)

s1 = 'programming'
print()

# 집합은 중복을 허용하지 않는다. {'i', 'g', 'n', 'p', 'r', 'o', 'm', 'a'}
print(set(s1)) 

# 리스트와 튜플은 순차적 자료형
print(list(s1)) # ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
print(tuple(s1)) # ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g')

'''
- 집합은 변경 가능한 자료형이어서 언제든지 데이터를 편집할 수 있다.
- 집합에 요소를 추가할 때는 add() 메서드를 사용하고, 제거할 때는 remove()를 사용한다.

'''

print('-'*40)

asia = {'korea', 'japan', 'taiwan', 'china'}
print(asia)

asia.add('thailand')
asia.add('china') # 기존 집합(asia) china가 있었고, 또 china를 추가했지만,
# 결과적으로 china는 하나만 출력된다.
asia.remove('japan')

print(asia)

asia2 = {'singapore', 'indonesia', 'korea'}

# print(asia + asia2) (x) set객체와 set객체를 합치려면 + 덧셈 연산으로는 합쳐지지 않는다. ----> set메서드를 사용하면 된다.
# 파이썬에서 제공하는 집합 연산자는 따로 있다.

asia.update(asia2)
print(asia)  