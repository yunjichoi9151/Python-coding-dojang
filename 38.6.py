# 파이썬 코딩 도장
# Chapter 38 연습문제

try:
    file = open('maria.txt', 'r')
except FileNotFoundError:
    print('파일이 없습니다.')
else:
    s = file.read()
    file.close()