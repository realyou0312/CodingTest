'''
백준1260
https://www.acmicpc.net/problem/1260

DFS와 BFS 기본문제

반복해서 숙달 필요.....

'''

N, M, V = map(int, input().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)] 

for i in range(M):
    from_n, to_n = map(int, input().split())
    matrix[from_n][to_n] = matrix[to_n][from_n] = 1 # 양쪽방향

visit_list = [0] * (N + 1)  # 인덱스0번 삭제

def dfs(start): # 재귀
    visit_list[start] = 1
    print(start, end=' ')
    for i in range(1, N + 1):
        if visit_list[i] == 0 and matrix[start][i] == 1:  # 방문 해야할 곳 선정
            dfs(i)


def bfs(start): # 큐
    queue = [start]
    visit_list[start] = 1
    
    while queue:
        start = queue.pop(0)
        print(start, end=' ')
        for i in range(1, N + 1):
            if visit_list[i] == 0 and matrix[start][i] == 1:
                queue.append(i)
                visit_list[i] = 1


dfs(V)
print()
visit_list = [0] * (N + 1)
bfs(V)