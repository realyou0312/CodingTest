'''
백준2294
https://www.acmicpc.net/problem/2294


풀이1. BFS
풀이2. DP
'''

from collections import deque

n, k =map(int, input().split())
coins = set(int(input()) for i in range(n))   # 같은 코인이 여러번 존재할 수 있기 때문에 set
check = [0 for i in range(k+1)]  # 사용한 동전의 최소값 확인용
q = deque()

for coin in coins:
    if coin > k:
        continue
    q.append([coin, 1])
    check[coin] = 1

check2 = True    # 불가능한 경우 확인
while q:
    val, cnt = q.popleft()
    if val == k:        # 하나씩 써내서 k와 비교
        print(cnt)
        check2 = False
        break

    for coin in coins:
        if val + coin > k:   # K보다 작으면
            continue
        if check[val + coin] == 0:
            check[val+coin] = 1
            q.append([val+coin, cnt+1])   # 큐에 넣어서 반복

if check2:
    print(-1)


