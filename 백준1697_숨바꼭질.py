#백준1697 : 숨바꼭질 - BFS
#https://www.acmicpc.net/problem/2178


from collections import deque

def bfs(n, k):
    q = deque([n])
    visited[n] = 1
    while q:
        now = q.popleft()
        for move in [now+1, now-1, now*2]: #이동 가능한 거리로 검사
            if 0<= move <= MAX and not visited[move]:
                visited[move] = 1
                q.append(move)
                dist[move] = dist[now]+1 #시간을 dist에 저장
    return dist[k]


n, k = map(int, input().split())
MAX = 200000 #원래 최대값 2배 = MAX
visited = [0] * (MAX+1)
dist = [0] * (MAX+1)
print(bfs(n,k))