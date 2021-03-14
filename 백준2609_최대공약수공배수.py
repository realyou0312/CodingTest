'''
백준2609
www.acmicpc.net/problem/2609

'''

# 유클리드 호제법 이용
# a, b에서 a%b = c 라고 한다면
# gcd(a,b) = gcd(b, c)  반복하면 a가 gcd


a, b = map(int, input().split())

def  gcd(a, b): 
    while b != 0:
        c = a%b
        a = b
        b = c
    return a

def lcm(a, b):
    lcm1 = a * b / gcd(a,b)
    return lcm1

print(gcd(a,b))
print(int(lcm(a,b)))
