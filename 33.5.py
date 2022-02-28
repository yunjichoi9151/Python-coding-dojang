# 파이썬 코딩 도장
# Chapter 33 연습문제

def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count 
 
c = counter()
for i in range(10):
    print(c(), end=' ')