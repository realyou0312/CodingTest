# 백준 4673번 셀프넘버
#acmicpc.net/problem/4673


array = [_ for _ in range(1,10001)]

for i in range(1, 10001):
    number = sum(map(int, str(i))) # 각 자리수의 합
    if i + number <= 10000 and i + number in array:
        a = i + number
        array.remove(a)

for i in range(len(array)):
    print(array[i])
