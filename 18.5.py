# 파이썬 코딩 도장
# Chapter 18 연습문제

i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end=' ')
    i += 1