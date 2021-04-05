#프로Lv.2 베스트앨범 - 해시
#https://programmers.co.kr/learn/courses/30/lessons/42579#


def solution(genres, plays):
    answer = []
    gen_play = {}  # 장르별 재생횟수 저장하는 dic
    gen_num = {}  # 장르별 재생횟수와 고유번호 저장하는 dic

    for i in range(len(genres)):
        if genres[i] in gen_play:
            gen_play[genres[i]] += plays[i]
            gen_num[genres[i]].append([plays[i], i])  # 이차원 배열 저장
        else:
            gen_play[genres[i]] = plays[i]  # 장르별로 재생횟수 각각 저장
            gen_num[genres[i]] = [[plays[i], i]]

    # 재생횟수 내림차순 정렬
    gen_play = sorted(gen_play.items(), key=lambda x: x[1], reverse=True)

    for i in gen_play:
        list = gen_num[i[0]]
        list = sorted(list, key=lambda x: x[0], reverse=True)  # ★★주의 장르 안에서 재정렬!!★★
        if len(list) == 1:  # 노래 1개 인 경우는 첫번째 고유번호만
            answer.append(list[0][1])
        else:
            answer.append(list[0][1])
            answer.append(list[1][1])

    return answer