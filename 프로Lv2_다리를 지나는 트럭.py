#프로그래머스 Lv.2 다리를 지나는 트럭 - 스택
#https://programmers.co.kr/learn/courses/30/lessons/42583


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_bridge = [0] * bridge_length # 다리 위에 있는 트럭
    while len(truck_bridge) > 0:
        answer += 1 # 1초씩 추가
        truck_bridge.pop(0)
        if truck_weights:
            if sum(truck_bridge) + truck_weights[0] <= weight: # 다리 한계 무게 체크
                truck_bridge.append(truck_weights.pop(0)) # 스택 쌓기
            else:
                truck_bridge.append(0)

    return answer