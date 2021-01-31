n,q=map(int, input().split())
xrhl=[]
for _ in range(n):
    x,r,h=map(int, input().split())
    xrhl.append((x,r,h))

MAX_H=2**10*4
hl=[0]*(MAX_H+1)
for bottom in range(MAX_H,-1,-1):
    ss=0
    for x,r,h in xrhl:
        # if x>=top: continue
        if x+h<=bottom:continue
        if x>=bottom:
            ss+=(r**2)*h
        else:
            parth=x+h-bottom
            partr=r*parth/h
            ss+=(partr**2)*parth
    hl[bottom]=ss

PI=3.14159265359
al=[]
for _ in range(q):
    a,b=map(int, input().split())
    ans=hl[a]-hl[b]
    ans*=PI
    ans/=3
    al.append(ans)

for a in al:print(a)