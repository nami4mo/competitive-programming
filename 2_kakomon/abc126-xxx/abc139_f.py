from math import atan2

n = int(input())
vl = []
for _ in range(n):
    x,y = map(int, input().split())
    deg = atan2(y,x)
    vl.append((deg,x,y))

vl.sort()
ans = 0
for i in range(n):
    for j in range(i,n):
        cx,cy = 0,0
        for k in range(i,j+1):
            cx += vl[k][1]
            cy += vl[k][2]
        d = cx**2+cy**2
        ans = max(d,ans)

for i in range(n):
    for j in range(n-1,-1,-1):
        if i > j: continue
        cx,cy = 0,0
        for k in range(i):
            cx += vl[k][1]
            cy += vl[k][2]
        for k in range(j,n):
            cx += vl[k][1]
            cy += vl[k][2]
        d = cx**2+cy**2
        ans = max(d,ans)

ans = ans**0.5
print(ans)