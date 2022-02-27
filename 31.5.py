# 파이썬 코딩 도장
# Chapter 31 심사문제

def fib(a):
    if a == 0 or a == 1:
        return a
    else:
        return fib(a - 2) + fib(a - 1)
 
n = int(input())
print(fib(n))