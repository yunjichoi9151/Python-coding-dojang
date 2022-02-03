# 파이썬 코딩 도장
# Chapter 21 연습문제

import turtle as t

n = 5
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right((360 / n) * 2)
    t.forward(100)
    t.left(360 / n)