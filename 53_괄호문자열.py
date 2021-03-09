def math(e):
    if e.count('(') != e.count(')'):
        return False
    a = []
    for i in e:
        if i == '(':
            a.append('(')
        if i == ')':
            if len(a) == 0:
                return False
            a.pop()
    return True

n = input()
if math(n) == True:
	print("YES")
else:
	print("NO")