n,q=map(int, input().split())
xyl_p=[]
xyl_m=[]
xyl=[]
for _ in range(n):
    x,y=map(int, input().split())
    xyl_p.append(x+y)
    xyl_m.append(x-y)
    xyl.append((x,y))

xyl_p.sort()
xyl_m.sort()

al=[]
for _ in range(q):
    qi=int(input())-1
    x,y=xyl[qi]
    xyp=x+y
    xym=x-y
    d1=xyl_p[-1]-xyp
    d2=xyp-xyl_p[0]
    d3=xym-xyl_m[0]
    d4=xyl_m[-1]-xym
    al.append(max(d1,d2,d3,d4))

for a in al:print(a)