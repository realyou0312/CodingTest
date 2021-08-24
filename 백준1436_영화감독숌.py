#백준1436번 영화감독 숌
#https://www.acmicpc.net/problem/1436

N = int(input())
first = 666 # 첫 666

while N != 0:
    if '666' in str(first):
        N = N-1
        if N == 0:
            break
    first = first + 1 # first 늘려가면서 확인
print(first)