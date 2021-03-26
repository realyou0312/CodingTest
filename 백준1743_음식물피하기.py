'''
백준1743
https://www.acmicpc.net/problem/1743


힌트 이용하기
'.' 을 초기화 한 이후에
'#'부분을 움식물의 좌표 위치로 바꿔준다

'''

from collections import deque

n, m, k = map(int, input().split())
matrix = [['.' for i in range(m)] for i in range(n)]
visited = [[0 for i in range(m)] for i in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0

for i in range(k):
    row, col = map(int, input().split())
    matrix[row-1][col-1] = '#'


def bfs(a, b):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):  # 4방위 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0: # 방문한 적이 없고
                if matrix[nx][ny] == '#':
                    q.append((nx,ny))
                    visited[nx][ny] = 1   # '#'이 연속으로 존재한다면
                    cnt += 1
    return cnt

for x in range(n):
    for y in range(m):
        if visited[x][y] == 0 and matrix[x][y] == '#':
            ans = max(ans, bfs(x,y))
print(ans)