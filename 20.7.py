# 파이썬 코딩 도장
# Chapter 20 연습문제

for i in range(1, 101):
    if i % 2 == 0 and i % 11 == 0:
        print('FizzBuzz')
    elif i % 2 == 0:
        print('Fizz')
    elif i % 11 == 0:
        print('Buzz')
    else:
        print(i)