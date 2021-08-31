# 백준 2751번 수 정렬하기2
# https://www.acmicpc.net/problem/2751

# 병합정렬 연습 - 시간복잡도 O(N)

# pypy3로 설정해야 시간초과 뜨지 않음

def merge_sort(array):
    if len(array) <= 1:
        return array

    # 재귀함수를 이용해서 끝까지 분할
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i ,j ,k = 0 ,0 ,0

    # 분할된 배열끼리 비교
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # 먼저 끝났을 때
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

n=int(input())
num = []

for _ in range(n):
    num.append(int(input()))

num = merge_sort(num)

for i in num:
    print(i)



# Sorted 함수
# 시간복잡도 NlogN 보장

n=int(input())
num=[]

for _ in range(n):
    x = int(input())
    num.append(x)

for i in sorted(num):
    print(i)