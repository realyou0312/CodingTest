#프로Lv.2 - 더맵게 - 힙
#https://programmers.co.kr/learn/courses/30/lessons/42626
# heapq 참고 - https://littlefoxdiary.tistory.com/3

import heapq

def solution(scoville, K):
    answer = 0
    h = []
    for i in scoville:
        heapq.heappush(h, i)  # h에 scoville 요소 값을 추가

    while h[0] < K:
        try:
            heapq.heappush(h, heapq.heappop(h) + (heapq.heappop(h)*2)) # 가장 작은수, 두번째로 작은수 로 scoville지수 연산
        except IndexError: # 인덱스 초과하는 경우 -1 반환 -> Case1 5 8 13번에 걸림
            return -1
        answer += 1
    return answer


# heappop은 가장 작은 요소를 제거하면서 그 수를 반환
