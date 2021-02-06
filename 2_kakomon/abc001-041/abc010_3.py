x1,y1,x2,y2,t,v=map(int, input().split())
n=int(input())
td=t*v

eps=10**(-8)
for _ in range(n):
    x,y=map(int, input().split())
    d1=(x1-x)**2+(y1-y)**2
    d2=(x2-x)**2+(y2-y)**2
    if d1**0.5+d2**0.5<=td+eps:
        print('YES')
        exit()
print('NO')