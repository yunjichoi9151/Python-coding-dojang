# 파이썬 코딩 도장
# Chapter 31 연습문제

def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])
 
print(is_palindrome('hello'))
print(is_palindrome('level'))