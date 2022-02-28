# 파이썬 코딩 도장
# Chapter 32 심사문제

files = input().split()
print(list(map(lambda x : '{0:03d}'.format(int(x.split('.')[0]))+ '.' + x.split('.')[1], files)))