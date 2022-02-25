# 파이썬 코딩 도장
# Chapter 24 심사문제

a = input().split()
count = 0
for i in a:
    if i.strip(',.') == 'the':
        count += 1
print(count)