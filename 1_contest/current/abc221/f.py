

def main():
    n=int(input())
    gl=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=map(int, input().split())
        a-=1
        b-=1
        gl[a].append(b)
        gl[b].append(a)

    if n==2:
        print(1)
        exit()

    root=-1
    for i in range(n):
        if len(gl[i])>=2:
            root=i
            break
    root_cs=gl[root][:]

    # print(root_cs)
    from collections import deque
    used=[-1]*n
    dists=[0]*n
    res=[]
    for root_c in root_cs:
        q=deque()
        q.append(root_c)
        used[root_c]=root_c
        cmax=0
        val=1
        while q:
            poped=q.popleft()
            # print(poped)
            for neib in gl[poped]:
                if used[neib]==root_c:continue
                if neib==root or neib==root_c:continue
                used[neib]=root_c
                dists[neib]=dists[poped]+1
                q.append(neib)
                if dists[neib]==cmax:
                    val+=1
                else:
                    cmax=dists[neib]
                    val=1
        res.append((cmax,val))
    # print(res)
    # print(dists)
    MOD=998244353
    ans=0
    res.sort(reverse=True)
    if res[0][0]==res[1][0]:
        vals=[]
        for d,cnt in res:
            if d!=res[0][0]:break
            vals.append(cnt)
        mul=1
        csum=0
        # print(vals)
        for v in vals:
            mul*=(v+1)
            mul%=MOD
            csum+=v
        ans=mul-csum-1
        ans%=MOD
        print(ans)
        # csum=sum(vals)
        # for v in vals:
        #     csum-=v
        #     ans+=csum*v
        #     ans%=MOD
        # print(ans)
    else:
        maxcnt=res[0][1]
        valsum=0
        for d,cnt in res[1:]:
            if d!=res[1][0]:break
            valsum+=cnt
        ans=maxcnt*valsum
        ans%=MOD
        print(ans)
        

if __name__ == "__main__":
    main()