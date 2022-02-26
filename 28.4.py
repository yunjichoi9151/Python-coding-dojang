# 파이썬 코딩 도장
# Chapter 28 심사문제

with open('words.txt', 'r') as file :
    words = file.readlines()
    for word in words:
        word = word.strip('\n')
        if word == word[::-1]:
            print(word)