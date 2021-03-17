'''
백준2293
https://www.acmicpc.net/problem/2293

유튜브 참고 - 점화식힌트
https://youtu.be/2IkdAk1Loek 
'''

# 적당한 점화식을 세우지 못하면 TIMEOUT

import stdin

n, k = map(int, sys.stdin.readline().split())
coins = []

for _ in range(n):
    coins.append(int(stdin.readline()))

coin_list = [0] * (k+1)

coin_list[0] = 1# 1원짜리 동전으로 1원 만드는 경우는 1가지

for i in coins:
    for j in range(i, k + 1 ):
        coin_list[j] += coin_list[j-i]
        
print(coin_list[k])


'''

        1  2  3  4  5  6  7  8  9  10
    1   1  1  1  1  1  1  1  1  1  1
    2   0  1  1  2  2  3  3  4  4  5
    5   0  0  0  0  1  1  2  2  3  4
           2  3  4  5  5  5  7  8  10  <- Total