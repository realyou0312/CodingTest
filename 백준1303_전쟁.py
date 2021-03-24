'''
백준1303
https://www.acmicpc.net/problem/1303


- 참고 -
https://dongdongfather.tistory.com/72

deque = 스택, 큐 기능을 같이 가진 객체

잘 써먹어 보기.

런타임오류 주의 -> 변수 초기화 항상 신경쓰기
'''

from collections import deque

def bfs():
    q.append((i,j)) # row, col 추가
    check[i][j] = 1
    cnt = 1
    while q:
        x, y = q.popleft() #좌측부터 시작
        for i in range(4):
            nx = x + dx[i]  # 4방향 체크
            ny = y + dy[i]
            # 완전 탐색!
            if (col > nx >= 0) and (row > ny >= 0) and matrix[nx][ny] == matrix[x][y] and check[nx][ny] == 0:
                check[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt

row, col = map(int, input().split())
matrix = [list(input()) for i in range(col)]
check = [[0] * row for i in range(col)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]  # 4방향
q = deque()
B = 0
W = 0


for i in range(col):
    for j in range(row):
        if check[i][j] == 0:
            ans = bfs()
            if matrix[i][j] == 'W':
                W += ans **2
            else:
                B += ans **2


print(W, B)
