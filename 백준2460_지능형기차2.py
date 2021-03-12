'''
백준2460
https://www.acmicpc.net/problem/2460

'''


p = 0
mp = 0
for i in range(10):
    a, b = map(int, input().split())
    if mp < p-a+b:
        mp = p-a+b
    p = p-a+b
print(mp)