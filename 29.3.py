# 파이썬 코딩 도장
# Chapter 29 연습문제

x = 10
y = 3
 
def get_quotient_remainder(a, b):
    return a // b, a % b
 
quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))