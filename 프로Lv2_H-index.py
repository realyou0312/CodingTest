#프로Lv.2 H-Index
#

# H-Index 부연설명 - https://www.ibric.org/myboard/read.php?Board=news&id=270333

def solution(citations):
    answer = 0
    citations = sorted(citations)

    for i in range(len(citations)):
        if citations[i] >= (len(citations)) - i:  # i번째 이상 cite 개수와 지금 cite 개수 비교
            answer = max(answer, len(citations)-i) # max조건 없으면 Case16 오류
            return answer


