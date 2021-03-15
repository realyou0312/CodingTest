'''

백준14888
https://www.acmicpc.net/problem/14888

'''

# DFS와 백트래킹으로 모든 경우 탐색
# 순열

N = int(input()) #숫자의 개수
a = list(map(int, input().split()))
c = list(map(int, input().split())) # 합이 N-1인 4개의 정수
ans_max = -1000000000       #문제 조건에 따른 정의
ans_min = 1000000000

def dfs(idx, ans):
    global ans_max, ans_min

    if idx == N:
        ans_max = max(ans_max, ans)
        ans_min = min(ans_min, ans)
        return

    if  c[0] > 0:
        c[0] -= 1
        dfs(idx+1, ans+a[idx])
        c[0] += 1
    if c[1] > 0:
        c[1] -= 1
        dfs(idx+1, ans-a[idx])
        c[1] += 1
    if c[2] > 0:
        c[2] -= 1
        dfs(idx+1, ans*a[idx])
        c[2] += 1
    if c[3] > 0:
        c[3] -= 1
        dfs(idx+1, int(ans/a[idx]))
        c[3] += 1

dfs(1, a[0])
print(ans_max)
print(ans_min)


'''

'''