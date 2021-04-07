#프로Lv.2 - 기능개발 : 스택
#https://programmers.co.kr/learn/courses/30/lessons/42586



def solution(progresses, speeds):
    answer = []
    day =0
    cnt = 0
    while len(progresses) != 0:
        #한 스택(day)에서 모든 경우 따지고 day 넘기기
        if progresses[0] + day * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            day += 1
    answer.append(cnt)
    return answer