from math import radians,sin,cos,atan2,degrees,sqrt

t=int(input())
l,x,y=map(int, input().split())

def e2yz(e):
    if e==0:return 0,0
    dist=360*(e/t)
    angle=-90-dist
    z1=sin(radians(angle))*(l/2)+l/2
    y1=cos(radians(angle))*(l/2)
    return y1,z1

for _ in range(int(input())):
    e=int(input())
    y1,z1=e2yz(e)
    dx=sqrt(x**2+(y-y1)**2)
    dz=z1
    angle=degrees(atan2(dz,dx))
    print(angle)