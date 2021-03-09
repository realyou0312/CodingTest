# 2021 카카오 공채 1번 문제:
# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3


def solution(new_id):
    answer = ''

#Level 1
    new_id = new_id.lower()

#Level 2 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word

#Level 3 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')

#Level 4 마침표(.)가 처음이나 끝에 위치한다면 제거
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]

#Level 5 빈 문자열이라면, new_id에 "a"를 대입
    if answer == '':
        answer = 'a'
#Level 6 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
#Level 7 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(answer) < 3:
        answer += answer[-1]

    return answer