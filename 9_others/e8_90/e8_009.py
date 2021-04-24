from math import degrees,atan2

def get_angle(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    angle=degrees(atan2(dy,dx))
    if angle<0:
        angle+=360
    return angle

def calc_angle(a1,a2):
    a=abs(a1-a2)
    if a>180:a=360-a
    return a

n=int(input())
xyl=[]
for _ in range(n):
    x,y=map(int, input().split())
    xyl.append((x,y))

from bisect import bisect_left, bisect_right

ans=0
for i in range(n):
    angles=[]
    x,y=xyl[i]
    for j in range(n):
        if i==j:continue
        x1,y1=xyl[j]
        angles.append(get_angle(x,y,x1,y1))
    angles.sort()
    for a in angles:
        target=a+180
        if target>=360:target-=360
        ind=bisect_right(angles, target)-1
        v=calc_angle(a,angles[ind])
        ans=max(ans,v)
        ind=bisect_left(angles, target)
        if ind<len(angles):
            v=calc_angle(a,angles[ind])
            ans=max(ans,v)

print(ans)