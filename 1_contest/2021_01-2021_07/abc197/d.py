n=int(input())
x,y=map(int, input().split())
xh,yh=map(int, input().split())
xc=(x+xh)/2
yc=(y+yh)/2

x-=xc
xh-=xc
y-=yc
yh-=yc

# ang=((n-2)*180)/n
ang=360/n

from math import cos,sin,radians
cosv=cos(radians(ang))
sinv=sin(radians(ang))

# print(x,y)
# print(ang,'ang')
# print(cosv)
# print(sinv)
ax=cosv*x-sinv*y
ay=sinv*x+cosv*y

ax+=xc
ay+=yc

print(ax,ay)