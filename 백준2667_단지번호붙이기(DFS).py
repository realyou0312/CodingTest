'''
백준2667
https://www.acmicpc.net/problem/2667


단지 = 1-1 연결되어 있는 트리

★시간단축!!

'''

size = int(input())
address = []  # 집의 유무
visit = [[0 for _ in range(size)] for _ in range(size)] # 방문기록 2차원으로 저장
ans = [] # 단지 내 집 개수
cnt = 0 # 단지 개수

for i in range(size):
    address.append(list(map(int, input())))

def DFS(row, col):
    if visit[row][col] == 0: # 방문하지 않았었다면
        visit[row][col] += 1
        if (address[row][col] == 1): # 집이 존재 한다면
            ans[cnt] += 1 # 현재 단지 번호에 해당하는 집 수 증가
            if (row > 0): # 좌측 이동 가능 여부
                if (visit[row-1][col] == 0):
                    DFS(row-1, col)   
            if (row < size-1): # 우측 이동 가능 여부
                if visit[row+1][col] == 0:
                    DFS(row+1,col)
            if (col > 0): # 위쪽 이동 가능 여부
                if visit[row][col-1] == 0:
                    DFS(row,col-1)
            if (col < size-1): # 아래쪽 이동 가능 여부
                if visit[row][col+1] == 0:
                    DFS(row,col+1)

for i in range(size):
    for j in range(size): # 모든 집 방문하면서
        if (visit[i][j] == 0 and address[i][j] == 1): # 방문X 집은 존재
            ans.append(0) # 단지 내 집 수
            cnt += 1 # 단지 추가
        DFS(i, j)  # 탐색

print(cnt+1) # 총 단지 숫자 (초기값이 0이었음)
ans.sort()
for i in range(len(ans)):
    print(ans[i])
