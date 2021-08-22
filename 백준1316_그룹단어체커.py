#백준1316 : 그룹 단어 체커
#https://www.acmicpc.net/problem/1316


# 그룹단어 : 연속해서 단어가 나타나는 경우


N = int(input())
result = N
for i in range(0,N):
    w =input()
    for j in range(0,len(w)-1):
        if w[j]==w[j+1]:
            pass
        elif w[j] in w[j+1:]:
            result-=1
            break
print(result)