'''
백준1292
https://www.acmicpc.net/problem/1292

'''

'''
Sol1 - Indexerror

def sol():
    A, B = map(int, input().split(' '))
    ar = []
    temp = 0
    cnt = 1

    

    for i in range(10):
        if temp == cnt:
            temp = 0
            cnt += 1
        ar.append(cnt)
        temp += 1

    result = 0
    for i in range(A-1, B):
        result += ar[i]
        
    print(result)

sol()

'''

#Sol2

A, B = map(int, input().split())
res, itr, cnt = 0, 1, 1

for i in range(1, B+1):
    if i >= A:
        res += itr
    if cnt >= itr:
        cnt = 0
        itr += 1
     
    cnt += 1
    
print(res)