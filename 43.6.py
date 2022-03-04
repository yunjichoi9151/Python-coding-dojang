# 파이썬 코딩 도장
# Chapter 43 심사문제
 
import re
p = re.compile('^(https?://)[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/.?=]*')
print(p.match(input()) != None)