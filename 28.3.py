# 파이썬 코딩 도장
# Chapter 28 연습문제

n = int(input())
text = input()
words = text.split()
 
if (len(words) < n):
    print('wrong')
else:
    n_gram = zip(*[words[i:] for i in range(n)])
    for i in n_gram:
        print(i)