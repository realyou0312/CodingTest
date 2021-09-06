# 백준 11004번 K번째 수
# https://www.acmicpc.net/problem/11004

# 풀이1

n, k = map(int, input().split())

nums = list(map(int, input().split()))

num = sorted(nums)
print(num[k-1])


# 풀이2


import sys
n, k = map(int, input().split())

nums = sys.stdin.readline().split(' ')

for i in range(len(nums)):
    nums[i] = int(nums[i])

nums = sorted(nums)
print(nums[k-1])

