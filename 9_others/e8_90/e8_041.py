def cross3(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

from collections import deque
def convex_hull(xyl):
    qs = deque()
    n = len(xyl)
    k = 0
    for p in xyl:
        while k > 1 and cross3(qs[-1], qs[-2], p) >=0:
            qs.pop()
            k-=1
        qs.append(p)
        k+=1
    t = k
    for i in range(n-2, -1, -1):
        p = xyl[i]
        while k > t and cross3(qs[-1], qs[-2], p) >= 0:
            qs.pop()
            k-=1
        qs.append(p)
        k+=1
    return list(qs)


def sum_of_floor(n,m,a,b):
    ans = 0
    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m
    if b >= m:
        ans += n * (b // m)
        b %= m
    y_max = (a * n + b) // m
    x_max = (y_max * m - b)
    if y_max == 0: 
        return ans
    ans += (n - (x_max + a - 1) // a) * y_max
    ans += sum_of_floor(y_max, a, m, (a - x_max % a) % a)
    return ans

# [x1,x2)
def get_lattice_cnt(x1,y1,x2,y2,rev=False):
    m=x2-x1
    if m==0:
        return abs(y2-y1)
    a=abs(y2-y1)
    b=0
    if (y1<=y2 and not rev) or (y1>y2 and rev):
        cnt=sum_of_floor(m,m,a,b)
    else:
        cnt=sum_of_floor(m+1,m,a,b)
    return cnt
    
# [x1,x2)
from math import gcd
def get_lattice_cnt_on_line(x1,y1,x2,y2):
    m=x2-x1
    if m==0: 
        return abs(y2-y1)
    a=abs(y2-y1)
    g=gcd(m,a)
    mg=m//g
    cnt=(m-1)//mg+1
    return cnt


n=int(input())
xyl=[]
for _ in range(n):
    x,y=map(int, input().split())
    xyl.append((x,y))

xyl.sort()
chxyl=convex_hull(xyl)
# print(chxyl)
lower=[]
upper=[]
lower_flag=True
xmi,xma=xyl[0][0],xyl[-1][0]
ymi,yma=10**18,-10**18
for x,y in chxyl:
    ymi=min(ymi,y)
    yma=max(yma,y)
    if lower_flag:
        if (x,y)==xyl[-1]:
            lower_flag=False
            lower.append((x,y))
            upper.append((x,y))
        else:
            lower.append((x,y))
    else:
        upper.append((x,y))
upper=upper[::-1]
# print(lower)
# print(upper)

del_cnt=0
line_lat_cnt=0
for i in range(len(lower)-1):
    x1,y1=lower[i]
    x2,y2=lower[i+1]
    box=(x2-x1)*(min(y1,y2)-ymi+1)
    tri=get_lattice_cnt(x1,y1,x2,y2)
    del_cnt+=(box+tri)
    line_lat_cnt+=get_lattice_cnt_on_line(x1,y1,x2,y2)


for i in range(len(upper)-1):
    x1,y1=upper[i]
    x2,y2=upper[i+1]
    box=(x2-x1)*(yma-max(y1,y2)+1)
    tri=get_lattice_cnt(x1,y1,x2,y2,True)
    del_cnt+=(box+tri)
    line_lat_cnt+=get_lattice_cnt_on_line(x1,y1,x2,y2)


if lower[-2][0]==lower[-1][0]:
    addcnt=abs(lower[-2][1]-lower[-1][1])
else:
    addcnt=0

squ=(xma-xmi)*(yma-ymi+1)
ans=squ-del_cnt+line_lat_cnt+1-n+addcnt


print(ans)
