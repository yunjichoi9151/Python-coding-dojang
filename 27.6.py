# 파이썬 코딩 도장
# Chapter 27 심사문제

with open('words.txt', 'r') as file:
    words = file.readline().split()
    for word in words:
        if 'c' in word:
            print(word.strip(',.'))