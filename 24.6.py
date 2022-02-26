# 파이썬 코딩 도장
# Chapter 24 심사문제

price = list(map(int,input().split(';')))
price.sort(reverse=True)
for i in price:
    print('{0:>9,}'.format(i))