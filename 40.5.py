# 파이썬 코딩 도장
# Chapter 40 연습문제

def file_read():
    with open('words.txt') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            yield line.strip('\n')
 
for i in file_read():
    print(i)