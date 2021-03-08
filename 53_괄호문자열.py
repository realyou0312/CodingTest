def math(e):
    if e.count('(') != e.count(')'):
        return False
    괄호 = []
    for i in e:
        if i == '(':
            괄호.append('(')
        if i == ')':
            if len(괄호) == 0:
                return False
            괄호.pop()
    return True

n = input()
if math(n) == True:
	print("YES")
else:
	print("NO")