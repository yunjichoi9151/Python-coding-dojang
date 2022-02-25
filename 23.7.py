# 파이썬 코딩 도장
# Chapter 23 심사문제

col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
for i in range(row):
    for j in range(col):
        if matrix[i][j] == '*':
            continue
        else:
            matrix[i][j] = 0
            for n in range(i-1, i+2):
                for m in range(j-1, j+2):
                    if n < 0 or m < 0 or n >= row or m >= col:
                        continue
                    elif matrix[n][m] == '*':
                        matrix[i][j] += 1

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end='')
    print()

    