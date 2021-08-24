#백준1476번 날짜계산 BFS
#https://www.acmicpc.net/problem/1476

e, s, m = map(int, input().split())

ans = 0
a, b, c, =0, 0, 0
while 1:
    if e == a and s == b and c == m:
        break
    a += 1
    b += 1
    c += 1
    ans += 1

    if a > 15:
        a %= 15
    if b > 28:
        b %= 28
    if c> 19:
        c %= 19

print(ans)