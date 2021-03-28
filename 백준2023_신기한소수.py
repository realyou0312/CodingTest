''''
백준2023
https://www.acmicpc.net/problem/2023

'''

N = int(input())

# 소수판별
def prime(a):
    if a == 0 or a == 1:
        return False
    else:
        for i in range(2, int(a**0.5)+1):
            if a % i == 0:
                return False
        return True

def DFS(a):
    if len(str(a)) == N:
        print(a)
    else:
        for i in range(10):  # 한자리수씩 붙이면서 소수 추가
            temp = a * 10 + i
            if prime(temp):
                DFS(temp)

# 한자리수 이하 소수
DFS(2)
DFS(3)
DFS(5)
DFS(7)