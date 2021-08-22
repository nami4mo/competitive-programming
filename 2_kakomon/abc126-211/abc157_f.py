def cross_p(x1,y1,r1,x2,y2,r2):
    x3=x2-x1
    y3=y2-y1
    a=(x3**2+y3**2+r1**2-r2**2)/2
    root=(x3**2+y3**2)*(r1**2)-a**2
    if root<0: return None,None,None,None
    root=root**0.5
    res_x1=(a*x3+y3*root)/(x3**2+y3**2)
    res_y1=(a*y3-x3*root)/(x3**2+y3**2)
    res_x2=(a*x3-y3*root)/(x3**2+y3**2)
    res_y2=(a*y3+x3*root)/(x3**2+y3**2)
    return res_x1+x1,res_y1+y1,res_x2+x1,res_y2+y1

# print(cross_p(0,1,5,4,3,5**0.5))


n,k=map(int, input().split())
if k==0:
    print(0)
    exit()

xycl=[]
for _ in range(n):
    x,y,c=map(int, input().split())
    xycl.append((x,y,c))

xycl.sort()

ok, ng = 3*(10**5), 0
while abs(ok-ng) > 10**(-8):
    t = (ok+ng)/2
    res = False
    xy_cands=[]
    for i in range(n):
        x1,y1,c1=xycl[i]
        r1=t/c1
        xy_cands.append((x1,y1))
        for j in range(i+1,n):
            x2,y2,c2=xycl[j]
            r2=t/c2
            a,b,c,d=cross_p(x1,y1,r1,x2,y2,r2)
            if a is None: continue
            xy_cands.append((a,b))
            xy_cands.append((c,d))
    for cx,cy in xy_cands:
        cnt=0
        for x,y,c in xycl:
            d2=(cx-x)**2+(cy-y)**2
            d=d2**0.5
            if d<=t/c+10**(-8): cnt+=1
        if cnt>=k:
            res=True
            break
    if res: ok = t
    else: ng = t
    # print(t)
print(ok)