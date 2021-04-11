#프로Lv.2 - 소수 찾기 : 완전탐색
#https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    answer = 0
    numlist = []
    for i in range(len(numbers)):
        temp = list(permutations(numbers, i+ 1))
        numlist += [int(''.join(j)) for j in temp]

    for i in set(numlist):  # set() -> 중복제거
        temp2 = 0
        for j in range(1, i + 1):  # 소수 판별
            if i % j == 0 and i != 0:
                temp2 += 1
            if temp2 >= 3:
                break
        if temp2 == 2:
            answer += 1
    return answer


# itertools.permutations
# n = '011'
# map(''.join, permutations(list(n), 2))
#'10', '01', '11'