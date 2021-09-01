#백준 2941번 크로아티아 알파벳
#https://www.acmicpc.net/problem/2941


'''
문제 조건 정리
1. 첫째줄 : 100글자 단어
2. 단어는 크로아티아 알파벳
3. 표 이외의 알파벳은 원래 알파벳

루틴
1. 리스트에 크로아티아 알파벳 하나씩 추가
2. 반복문으로 문자열에서 크로아티아 찾으면 문자열에서 제외시킴

'''


string = input()
alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in alpha:
   if i in string:
       string = string.replace(i," ")
print(len(string))