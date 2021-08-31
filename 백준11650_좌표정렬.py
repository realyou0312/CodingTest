# 백준 11650번 좌표 정렬하기
# https://www.acmicpc.net/problem/11650


n = int(input())
xy = [[0]*2 for i in range(n)]

for i in range(n):
    temp_x, temp_y = input().split()
    xy[i][0] = int(temp_x)
    xy[i][1] = int(temp_y)

# xy의 첫번째값을 기준으로 오름차순 정렬한 다음 두번째값을 기준으로 정렬
res = sorted(xy, key= lambda x : (x[0], x[1]))

for i in range(n):
    print('%d %d' % (res[i][0], res[i][1]))