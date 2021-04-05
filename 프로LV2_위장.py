# 프로그래머스LV.2 위장 - 해시
# https://programmers.co.kr/learn/courses/30/lessons/42578


def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        tmp = i[1]
        if dic.get(tmp):    # 의상 개수 카운트
            dic[tmp] += 1
        else:
            dic[tmp] = 2    # 의상을 선택하지 않는 경우 첫 딕셔너리에 1 추가
    for i in dic.values():
        answer *= i
    return answer-1     # 의상을 입지 않은 경우 제외하고 리턴