'''
* 리스트 내부 요소 삭제
1. remove(): 삭제할 값을 직접 지정하여 삭제
2. 내장함수 del(): 삭제할 요소의 인덱스를 통해 삭제합니다.
3. clear(): 리스트 내부 요소 전체 삭제
'''

points = [1,2,3,4,5,6,7,8,9]

points.remove(1) # 값을 직접 지정
print(points)

del(points[2]) #del points[2] --> 소괄호 생략 가능 #리스트의 인덱스를 지정해서
# 해당하는 리스트의 인덱스의 요소를 삭제
print(points)

points.clear()
print(points)