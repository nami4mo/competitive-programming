n=int(input())
xyl=[]
for _ in range(n):
    x,y=map(int, input().split())
    xyl.append((x,y))
xyl.sort()

from math import atan2, degrees
from bisect import bisect_left, bisect_right

don=0
choku=0
eps=10**(-8)
for i in range(n):
    x,y=xyl[i]
    degs=[]
    for j in range(n):
        if i==j:continue
        xx,yy=xyl[j]
        deg=degrees(atan2(yy-y, xx-x))
        degs.append(deg)
        degs.append(deg+360)
    degs.sort()
    for d in degs[:n-1]:
        c180=bisect_left(degs, d+180)
        c90_1=bisect_left(degs, d+90+eps)
        c90_2=bisect_left(degs, d+90-eps)

        choku_c=c90_1-c90_2
        don_c=c180-c90_1
        choku+=choku_c
        don+=don_c

ei=n*(n-1)*(n-2)//6 - (choku+don)
print(ei, choku, don)
