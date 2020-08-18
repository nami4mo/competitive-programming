s = input()
a = s.count('a')
b = s.count('b')
c = s.count('c')

n = len(s)
if n%3 == 0:
    if a == b and b == c:
        print('YES')
    else:
        print('NO') 

elif n%3 == 1:
    v = [a,b,c]
    v.sort()
    if v[0] == v[1] and v[1]+1 == v[2]:
        print('YES')
    else:
        print('NO')


elif n%3 == 2:
    v = [a,b,c]
    v.sort()
    if v[0]+1 == v[1] and v[1] == v[2]:
        print('YES')
    else:
        print('NO')