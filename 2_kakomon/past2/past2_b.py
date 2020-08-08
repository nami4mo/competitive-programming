s = str(input())

a = s.count('a')
b = s.count('b')
c = s.count('c')

if a > b and a > c:
    print('a')
elif b > a and b > c:
    print('b')
else:
    print('c')