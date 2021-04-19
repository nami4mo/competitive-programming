# y=ax+b, y=cx+d
def get_cross_point(a,b,c,d):
    x=(d-b)/(a-c)
    y=a*x+b
    return x,y

def two_point_line(x1,y1,x2,y2):
    a=(y2-y1)/(x2-x1)
    b=-a*x1+y1
    return a,b

from math import sqrt
def get_dist(x1,y1,x2,y2):
    d=sqrt((x1-x2)**2+(y1-y2)**2)
    return d

x0,y0=map(int, input().split())
n=int(input())
xyl=[]
for _ in range(n):
    x,y=map(int, input().split())
    x-=x0
    y-=y0
    xyl.append((x,y))
xyl.append(xyl[0])

ans=10**10
for i in range(n):
    x1,y1=xyl[i]
    x2,y2=xyl[i+1]
    dx=x2-x1
    dy=y2-y1

    d=get_dist(0,0,x1,y1)
    ans=min(ans,d)

    if dx==0:
        cx=x1
        cy=0
        if not(y1<=0<=y2 or y2<=0<=y1):continue
        d=abs(cx-x0)
        ans=min(ans,d)
    elif dy==0:
        cx=0
        cy=y1
        if not(x1<=0<=x2 or x2<=0<=x1):continue
        d=abs(cy-y0)
        ans=min(ans,d)
    else:
        a,b=two_point_line(x1,y1,x2,y2)
        c= -1/a
        x,y=get_cross_point(a,b,c,0)
        if not(x1<=x<=x2 or x2<=x<=x1):continue
        d=get_dist(0,0,x,y)
        ans=min(ans,d)
print(ans)
