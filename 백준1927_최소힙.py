#백준1927 : 최소힙 - Heapq
#https://www.acmicpc.net/problem/1927


# 참고 - https://covenant.tistory.com/143?category=874690

import heapq
import sys
input=sys.stdin.readline # 개행문자 제거하여 시간 단축

arr = []
N = int(input())
i = 0
while i < N:
    n = int(input())
    if n:
        heapq.heappush(arr, n)
    else:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    i += 1