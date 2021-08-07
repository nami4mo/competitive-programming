n=int(input())
x0,y0=map(int, input().split())
x1,y1=map(int, input().split())

from math import atan2,cos,sin

ddx=x1-x0
ddy=y1-y0
angle=atan2(ddy,ddx)
da=-angle

dx=(x0+x1)/2
dy=(y0+y1)/2

for _ in range(n):
    x,y=map(int, input().split())
    x-=dx
    y-=dy
    x,y=cos(da)*x-sin(da)*y, sin(da)*x+cos(da)*y
    print(x,y)