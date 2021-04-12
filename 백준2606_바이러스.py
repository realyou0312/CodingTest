#백준2606번 - 바이러스 - 완전탐색 : 인접리스트
#https://www.acmicpc.net/problem/2606



# 참고 - 그래프이론 인접행렬, 인접리스트
#https://duwjdtn11.tistory.com/515

from collections import deque

n = int(input())  # 컴퓨터 대수
check = [0] * (n + 1)
com = [[] for i in range(n + 1)]  # 전체 컴퓨터 - 2차원 배열

for i in range(int(input())): # 인접리스트
    a, b = map(int, input().split())  # 연결된 PC
    com[a].append(b)
    com[b].append(a)

check[1] = 1 # 자기자신
q = deque([1])
while q:
    x = q.popleft()
    for i in range(len(com[x])):
        if check[com[x][i]] == 0:
            q.append(com[x][i])
            check[com[x][i]] = 1

print(sum(check) - 1)