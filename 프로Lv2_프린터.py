# 프로그래머스 Lv.2 - 프린터 : 스택/큐
#https://programmers.co.kr/learn/courses/30/lessons/42587


# max, pop 이용
def solution(priorities, location):
    answer = 0
    while len(priorities): #중요도 순 케이스 분류
        if priorities[0] == max(priorities): #중요도 높은 문서 가장 앞인 경우
            answer += 1
            priorities.pop(0)
            if location == 0:
                return answer
            else: location -= 1
        else:
            priorities.append(priorities.pop(0)) #맨 뒤로 이동
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer

# 큐 사용
# from collections import deque
# def solution(priorities, location):
#     answer = 0
#     arr = deque([(i, j) for j, i in enumerate(priorities)]) #value와 index값 사용
#     while len(arr):
#         item = arr.popleft() #시간복잡도 O(1) : 대기번호 1번
#         if arr and max(arr)[0] > item[0]:
#             arr.append(item)
#         else:
#             answer += 1
#             if item[1] == location:
#                 break
#     return answer
