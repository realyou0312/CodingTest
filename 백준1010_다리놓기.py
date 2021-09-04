# 백준 1010번 다리놓기
# https://www.acmicpc.net/problem/1010



# 조합문제

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n) * factorial(m - n))
    print(bridge)