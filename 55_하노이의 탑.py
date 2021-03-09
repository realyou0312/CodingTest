'''
문제55 : 하노이의 탑

하노이의 탑은 프랑스 수학자 에두아르드가 처음으로 발표한 게임입니다. 하노이의 탑은 A, B, C 3개의 기둥과 기둥에 꽂을 수 있는 N개의 원판으로 이루어져 있습니다. 이 게임에서 다음의 규칙을 만족해야 합니다.

1. 처음에 모든 원판은 A기둥에 꽂혀 있다.
2. 모든 원판의 지름은 다르다.
3. 이 원반은 세 개의 기둥 중 하나에 반드시 꽂혀야 한다.
4. 작은 원반 위에 큰 원반을 놓을 수 없다.
5. 한 번에 하나의 원판(가장 위에 있는 원판) 만을 옮길 수 있다.

이 규칙을 만족하며 A기둥에 있는 원반 N개를 모두 C 원반으로 옮기고 싶습니다.
모든 원반을 옮기기 위해 실행되어야 할 최소 원반 이동 횟수를 계산하는 프로그램을 완성해주세요.
'''

path = []
def solution(num, col_st, col_ob, col_sb):

    if num == 1:
        path.append([col_st, col_ob])
        return None
    
    #원반 n-1개 중간기둥으로 옮기기
    solution(num-1, col_st, col_sb, col_ob)

    #가장 큰 원반 object로 설정
    path.append([col_st, col_ob])

    #서브기둥과 시작기둥 바꾸기
    solution(num-1, col_sb, col_st, col_ob)

solution(3, 'A', 'C', 'B')
print(path)
print(len(path))

