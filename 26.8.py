# 파이썬 코딩 도장
# Chapter 26 연습문제

a = {i for i in range(1, 101) if i % 3 == 0}
b = {i for i in range(1, 101) if i % 5 == 0}

print(a & b)