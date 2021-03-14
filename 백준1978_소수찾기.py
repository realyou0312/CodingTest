'''
백준1978
https://www.acmicpc.net/problem/1978

'''

# N개 중에서 소수가 몇개인지 출력

n = int(input())
numlist = [int(i) for i in input().split()]

prime = 0

for i in numlist:
    if i != 1:
        if i == 2:
            prime += 1
        else:
            for j in range(2, i):       # 소수 판단
                if i % j ==0:
                    break

                elif j == i -1:
                    prime += 1

print(prime)