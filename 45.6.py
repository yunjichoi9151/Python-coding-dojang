# 파이썬 코딩 도장
# Chapter 45 연습문제
# 여러 파일을 같이 묶어놓아 모두 주석으로 처리했습니다.

'''database/__init__.py

from .sqlite.dbapi import *
'''

'''database/sqlite/__init__.py

# 내용이 비어 있음
'''

'''database/sqlite/dbapi.py

def connect(database):
    print(database)
'''

'''practice_package.py

from database import *
 
connect(':memory:')
'''