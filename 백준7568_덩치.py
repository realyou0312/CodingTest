'''
백준7568
https://www.acmicpc.net/problem/7568

'''

#브루트포스 문제
# 처음부터 rank를 지정해서 덩치를 비교하고 하나씩 올리기

N=int(input())
dung_list = []
for i in range(N):
    x, y = map(int,input().split())
    dung_list.append((x,y))

for i in dung_list:
    rank = 1
    for j in dung_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    
    print(rank)

