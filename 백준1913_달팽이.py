#백준 1913번 달팽이
#https://www.acmicpc.net/problem/1913

N = int(input())
m = int(input())
array = [[0 for _ in range(N)] for _ in range(N)]
n = 1

x, y = N // 2, N // 2
check = 2
array[x][y] = n
i = 0
j = 0
while array[0][0] != N ** 2:
    x -= 1
    for i in range(check):
        n += 1
        array[x][y + i] = n
        if n == m:
            ans = [x + 1, y + i + 1]
    y += i
    for i in range(1, check + 1):
        n += 1
        array[x + i][y] = n
        if n == m:
            ans = [x + i + 1, y + 1]
    x += i
    for i in range(1, check + 1):
        n += 1
        array[x][y - i] = n
        if n == m:
            ans = [x + 1, y - i + 1]
    y -= i
    for i in range(1, check + 1):
        n += 1
        array[x - i][y] = n
        if n == m:
            ans = [x - i + 1, y + 1]
    x -= i
    check += 2

for i in range(N):
    for j in range(N):
        print(array[i][j], end=' ')
    print()
print(ans)


# 실패
'''
n = int(input())
m = int(input())


x, y = n // 2, n // 2
mx, my = x, y
dx = [-1, 0, 1, 0] #방향
dy = [0, 1, 0, -1]

pre_d = 0
d = 0 # 방향 설정용
array = [[0 for _ in range(n)] for _ in range(n)]
array[x][y] = 1
cnt = 2

while True:
    if x == 0 and y == 0:
        break

    if array[x + dx[d]][y + dy[d]] == 0:
        x += dx[d]  # 보는 방향으로 이동
        y += dy[d]
        pre_d = d
        d = d + 1 if d != 3 else 0 # 3인 경우 1로 변경
    else:
        x += dx[pre_d]
        y += dy[pre_d]
    array[x][y] = cnt
    if cnt == m:
        mx, my = x + 1, y + 1
    cnt += 1

for i in range(n):
    for j in range(n):
        print(array[i][j], end=' ')
    print()
print(mx, my)
'''