'''
백준2178
https://www.acmicpc.net/problem/2178

BFS
- 최소이동 카운트가 핵심
    -> 차수를 따지는 변수에 따로 저장해서 최종적으로 도착위치의 노드 차수가 최소이동횟수


'''


[N, M] = list(map(int, input().split()))
maze = []
visited = [[0 for _ in range(M)] for _ in range(N)] # 방문여부
counter = [[0 for _ in range(M)] for _ in range(N)] # 차수
Q = [] # 방문순서 기록하는 큐

for i in range(N):
    maze.append(list(map(int, input()))) 

def BFS():
    while(len(Q)>0):
        [row, col] = Q.pop(0)

        if (row>0): # 동서남북 확인
            if (visited[row-1][col]==0 and maze[row-1][col] == 1): #방문하지 않았거나 미로가 1
                Q.append([row-1,col])
                visited[row-1][col] = 1 
                counter[row-1][col] += counter[row][col]+1 

        if (col>0):
            if (visited[row][col-1]==0 and maze[row][col-1] == 1):
                Q.append([row,col-1])
                visited[row][col-1]=1
                counter[row][col-1] += counter[row][col]+1

        if (row<N-1):
            if (visited[row+1][col]==0 and maze[row+1][col] == 1):
                Q.append([row+1,col]) 
                visited[row+1][col]=1
                counter[row+1][col] += counter[row][col]+1

        if (col<M-1):
            if (visited[row][col+1]==0 and maze[row][col+1] == 1):
                Q.append([row,col+1])
                visited[row][col+1]=1
                counter[row][col+1] += counter[row][col]+1

        
Q.append([0,0]) #시작점
visited[0][0] = 1
counter[0][0] = 1
BFS()
print(counter[N-1][M-1]) 