#백준 1018번 체스판 다시 칠하기
#https://www.acmicpc.net/problem/1018

# 참고 : https://huidea.tistory.com/127

n, m = map(int, input().split())
m_list = []
for _ in range(n):
    m_list.append(input())
n_min = 64

for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = 0
        cnt2 = 0
        for k in range(i, i + 8):
            for s in range(j, j + 8):
                if k % 2 == 0 and s % 2 == 0:
                    if m_list[k][s] == 'B':
                        cnt1 += 1
                elif k % 2 == 1 and s % 2 == 1:
                    if m_list[k][s] == 'B':
                        cnt1 += 1
                elif k % 2 == 0 and s % 2 == 1:
                    if m_list[k][s] == 'W':
                        cnt1 += 1
                elif k % 2 == 1 and s % 2 == 0:
                    if m_list[k][s] == 'W':
                        cnt1 += 1
        for k in range(i, i + 8):
            for s in range(j, j + 8):
                if k % 2 == 0 and s % 2 == 0:
                    if m_list[k][s] == 'W':
                        cnt2 += 1
                elif k % 2 == 1 and s % 2 == 1:
                    if m_list[k][s] == 'W':
                        cnt2 += 1
                elif k % 2 == 0 and s % 2 == 1:
                    if m_list[k][s] == 'B':
                        cnt2 += 1
                elif k % 2 == 1 and s % 2 == 0:
                    if m_list[k][s] == 'B':
                        cnt2 += 1
        n_min = min(n_min, cnt1, cnt2) # 첫 시작이 'W'인 경우, 'B'인 경우 중 작은값 저장
print(n_min)