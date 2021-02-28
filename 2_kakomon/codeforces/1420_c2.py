import sys
input = sys.stdin.readline
ansl=[]
for _ in range(int(input())):
    n,q=map(int, input().split())
    al=list(map(int, input().split()))
    if n==1:
        ansl.append(al[0])
        for _ in range(q):
            l,r=map(int, input().split())
            ansl.append(al[0])
        continue

    al=[-100]+al+[-100]
    ud=[0]*(n+2)
    ans=0
    for i in range(1,n+1):
        if al[i-1]>al[i] and al[i]<al[i+1]:
            ud[i]=-1
            ans-=al[i]
        elif al[i-1]<al[i] and al[i]>al[i+1]:
            ud[i]=1
            ans+=al[i]
    # if al[0]>al[1]:
    #     ud[0]=1
    #     ans+=al[0]
    # if al[-2]<al[-1]:
    #     ud[-1]=1
    #     ans+=al[-1]
    ansl.append(ans)
    for _ in range(q):
        l,r=map(int, input().split())
        # l-=1
        # r-=1
        # pl=ud[l]*al[l]
        # pr=ud[r]*al[r]
        # ans-=pl
        # ans-=pr
        changed=set()
        for i in [-1,0,1]:
            ll=l+i
            rr=r+i
            if 0<ll<n+1 and ll not in changed: 
                ans-=ud[ll]*al[ll]  
                changed.add(ll)
            if 0<rr<n+1 and rr not in changed: 
                ans-=ud[rr]*al[rr]    
                changed.add(rr)        

        changed=set()
        al[l],al[r]=al[r],al[l]
        for i in [-1,0,1]:
            ll=l+i
            if not 0<ll<n+1:continue
            if al[ll-1]>al[ll] and al[ll]<al[ll+1]:
                ud[ll]=-1
                ans-=al[ll]
                changed.add(ll)
            elif al[ll-1]<al[ll] and al[ll]>al[ll+1]:
                ud[ll]=1
                ans+=al[ll]  
                changed.add(ll)
            else:
                ud[ll]=0  

        for i in [-1,0,1]:
            rr=r+i
            if not 0<rr<n+1:continue
            if rr in changed:continue
            # if rr in [l-1,l,l+1]:continue
            if al[rr-1]>al[rr] and al[rr]<al[rr+1]:
                ud[rr]=-1
                ans-=al[rr]
            elif al[rr-1]<al[rr] and al[rr]>al[rr+1]:
                ud[rr]=1
                ans+=al[rr]    
            else:
                ud[rr]=0  
        # print(ud)
        ansl.append(ans)

for a in ansl:print(a)