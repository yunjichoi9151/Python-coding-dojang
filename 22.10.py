# 파이썬 코딩 도장
# Chapter 22 심사문제

start, stop = map(int, input().split())
list = [2 ** i for i in range(start, stop + 1)]
del list[1]
del list[-2]
print(list)