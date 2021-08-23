



n, k = map(int, input().split())
nums = [p for p in range(1, n+1)]
answer = []
temp = k-1
for i in range(n):
    if len(nums) > temp: # 위치가 리스트를 넘지않으면
        answer.append(nums.pop(temp)) # 제거하고 답으로 추가
        temp += k-1 # temp번째 수가 제거 되었고 (k-1)만큼 다음수가 시작
    elif len(nums) <= temp: # 위치가 리스트를 넘으면
        temp = temp % len(nums) # (나눠주어야 한사람으로 카운트)
        answer.append(nums.pop(temp)) # 제거하고 답으로 추가
        temp += k-1 # temp번째 수가 제거 되었고 (k-1)만큼 다음수가 시작이므로
print('<', end='')
for i in answer:
    if i == answer[-1]:
        print(i, end='')
    else:
        print("%s, " % i, end='')
print('>',end='')