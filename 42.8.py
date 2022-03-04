# 파이썬 코딩 도장
# Chapter 42 심사문제

def html_tag(tag_name):
    def real_decorator(func):
        def wrapper():
             return '<{0}>{1}</{0}>'.format(tag_name, func())
        return wrapper
    return real_decorator

a, b = input().split()
 
@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'
 
print(hello())