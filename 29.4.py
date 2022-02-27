# 파이썬 코딩 도장
# Chapter 29 심사문제

x, y = map(int, input().split())
 
def calc(a, b):
    return a + b, a - b, a * b, a / b

a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))