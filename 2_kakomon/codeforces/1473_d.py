ansl=[]
for _ in range(int(input())):
    n,m=map(int, input().split())
    s=input()
    cma,cmi=0,0
    cv=0
    maxs=[0]
    mins=[0]
    vs=[0]
    for si in s:
        if si=='+':cv+=1
        else: cv-=1
        cma=max(cma,cv)
        cmi=min(cmi,cv)
        maxs.append(cma)
        mins.append(cmi)
        vs.append(cv)
    
    last_v=cv
    cma,cmi=last_v,last_v
    cv=last_v
    maxs_r=[0]*(n+1)
    mins_r=[0]*(n+1)
    maxs_r[n]=cma
    mins_r[n]=cmi
    # for si in s:
    for i in range(n-1,-1,-1):
        si=s[i]
        if si=='+':cv-=1
        else: cv+=1
        cma=max(cma,cv)
        cmi=min(cmi,cv)
        maxs_r[i]=cma
        mins_r[i]=cmi

    # print(vs)
    # print(mins)
    # print(maxs_r)
    # print(mins_r)
    for _ in range(m):
        l,r=map(int, input().split())
        l-=1
        r-=1
        drop=vs[r+1]-vs[l]
        ma=maxs[l]
        mi=mins[l]
        maa=maxs_r[r+1]-drop
        mii=mins_r[r+1]-drop
        maaa=max(maa,ma)
        miii=min(mi,mii)
        ans=maaa-miii+1
        ansl.append(ans)

for a in ansl:print(a)