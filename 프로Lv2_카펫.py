#프로Lv.2 - 카펫 : 완전탐색
#https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    for a in range(1, yellow//2 + 2): # a=노란 카펫 가로 b=노란 카펫 세로길이
        if yellow%a == 0:
            b = yellow//a
            sq_yellow = a*b
            sq_brown = (a+2)*(b+2)
            if sq_brown-sq_yellow == brown:
                return [b+2, a+2]