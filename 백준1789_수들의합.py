#백준 1789번 수들의 합
#https://www.acmicpc.net/problem/1789


s = int(input())

for i in range(1, s+1):
    if s - i < 0: # S를 최대한 작은수로만 더해서 만들어야 함
        break
    s -= i
    res = i

print(res)