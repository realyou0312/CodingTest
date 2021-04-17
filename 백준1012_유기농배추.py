#백준1012 : BFS
#https://www.acmicpc.net/problem/1012


from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y, cnt_temp):
    q = deque()
    q.append((x, y))
    matrix[x][y] = cnt_temp

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1 and matrix[nx][ny] == -1:
                    q.append((nx, ny))
                    matrix[nx][ny] = cnt_temp


t = int(input())
for i in range(t):
    cnt = 0
    n, m, b = map(int, input().split())  # b=덩어리 개수까지 찾기
    a = [[0] * m for _ in range(n)]
    matrix = [[-1] * m for _ in range(n)]

    for _ in range(b):
        i, j = map(int, input().split())
        a[i][j] = 1

    for i in range(n):  #BFS 탐색
        for j in range(m):
            if a[i][j] == 1 and matrix[i][j] == -1:
                cnt += 1
                bfs(i, j, cnt)
print(cnt)