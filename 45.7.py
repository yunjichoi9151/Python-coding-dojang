# 파이썬 코딩 도장
# Chapter 45 심사문제
# 여러 파일을 같이 묶어놓아 모두 주석으로 처리했습니다.

'''calcpkg/__init__.py

# 내용이 비어 있음
'''

'''calcpkg/operation.py

import math
 
def squareroot(n):
    return math.sqrt(n)
'''

'''calcpkg/geometry.py

import math
 
def circle_area(radius):
    return radius * radius * math.pi
'''

'''judge_package.py

from calcpkg import operation, geometry

r = int(input())
print(operation.squareroot(r))
print(geometry.circle_area(r))
'''