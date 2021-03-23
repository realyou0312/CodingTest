'''
백준3085
https://www.acmicpc.net/problem/3085

Idea
1. 사탕을 서로 교환
2. 완전탐색으로 최대값 찾기 (가로, 세로)

'''

def row(a): # row 사탕 최대값
    maxnum = 1
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if (a[i][j] == a[i][j-1]):
                cnt += 1
                maxnum = max(maxnum, cnt)
            else:
                cnt = 1
    return maxnum

def col(a): # col 사탕 최대값
    maxnum = 1
    for j in range(n):
        cnt = 1
        for i in range(1,n):
            if (a[i][j] == a[i-1][j]):
                cnt += 1
                maxnum = max(maxnum, cnt)
            else:
                cnt = 1
    return maxnum

n = int(input())

matrix = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    a = list(input())
    for j in range(n):
        matrix[i][j]=a[j]

temp = 0
result = 0

for i in range(n):      # 가로 사탕 교환
    for j in range(n-1):
        if (matrix[i][j] != matrix[i][j+1]):
            temp = matrix[i][j]           # 교환
            matrix[i][j] = matrix[i][j+1]
            matrix[i][j+1] = temp
            if row(matrix) > result:      # 최대값 판단
                result = row(matrix)
            else:
                result
            if col(matrix) > result:      # 최대값 판단
                result = col(matrix)
            else:
                result
            temp = matrix[i][j]             # 다시 교환(원위치)
            matrix[i][j] = matrix[i][j+1]
            matrix[i][j+1] = temp          

for i in range(n-1):        # 세로 사탕 교환
    for j in range(n):
        if (matrix[i][j] != matrix[i+1][j]):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i+1][j]
            matrix[i+1][j] = temp
            if row(matrix) > result:
                result = row(matrix)
            else:
                result
            if col(matrix) > result:
                result = col(matrix)
            else:
                result
            temp = matrix[i][j]
            matrix[i][j] = matrix[i+1][j]
            matrix[i+1][j] = temp          

print(result)