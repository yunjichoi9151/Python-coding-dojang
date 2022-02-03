# 파이썬 코딩 도장
# Chapter 19 연습문제

for i in range(5):
    for j in range(5):
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    print()