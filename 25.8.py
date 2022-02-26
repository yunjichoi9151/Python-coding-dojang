# 파이썬 코딩 도장
# Chapter 25 심사문제

keys = input().split()
values = map(int, input().split())
 
x = dict(zip(keys, values))
 
x = {key: value for key, value in x.items() if key != 'delta' and value != 30}
 
print(x)