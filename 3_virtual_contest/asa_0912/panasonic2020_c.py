a,b,c = map(int, input().split())
r = c-a-b
if r < 0:
    print('No')
else:
    l = 4*a*b
    if l < r**2:
        print('Yes')
    else:
        print('No')