# 파이썬 코딩 도장
# Chapter 21 심사문제

import turtle as t

n, line = map(int, input().split())
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.forward(line)
    t.right((360 / n) * 2)
    t.forward(line)
    t.left(360 / n)