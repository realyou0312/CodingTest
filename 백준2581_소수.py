'''
백준2581
https://www.acmicpc.net/problem/2581

'''

a = int(input())
b = int(input())  # a이상 b이하의 수

prime = []

for i in range(a, b+1):
    prime_check = True   # 소수인지 아닌지 체크

    for j in range(2, i):
        if i % j == 0:
            prime_check = False
            break
    
    if i == 1:
            prime_check = False
        
    if prime_check == True:
            prime.append(i)    # 소수인 값들만 리스트에 추가

prime_sum = 0
for i in range(len(prime)):
    prime_sum += prime[i]

if len(prime) < 1:    # 소수가 없으면 -1 출력
    print(-1)

else:   # 소수가 있으면 prime sum과 가작 작은 소수 출력
    print(prime_sum)
    print(prime[0])