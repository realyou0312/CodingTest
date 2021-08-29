# 백준1475번 방 번호
# https://www.acmicpc.net/problem/1475


n = list(map(int, input())) # 9999
arr = [0 for _ in range(10)] # 인덱스를 가지는 리스트
for i in range(len(n)):
    arr[n[i]] += 1 # [0,0,0,0,0,0,0,0,0,9]
arr[6] += arr[9] # 6과 9는 6에 몰아서 담기
arr[9] = 0
cnt = 0
while sum(arr) > 0:
    for i in range(len(arr)):
        if arr[i] > 0 and i != 6:
            arr[i] -= 1
        if arr[i] > 0 and i == 6:
            if arr[i] % 2 == 0:
                arr[i] -= 2
            else:
                arr[i] -= 1
    cnt += 1
print(cnt)
