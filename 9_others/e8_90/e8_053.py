INF=-(10**10)
def query(n, i, al):
    if i>n:
        return n-i-1+INF
    if al[i]!=INF:
        return al[i]
    print('?', i, flush=True)
    res=int(input())
    al[i]=res
    return res

fib=[1,1]
for i in range(13):
    fib.append(fib[-1]+fib[-2])

for _ in range(int(input())):
    n=int(input())
    if n<=15:
        al=[INF]*(n+1)
        ans=-10
        for i in range(n):
            ans=max(ans,query(n,i+1,al))
        print('!',ans)
        continue

    N=1597
    al=[INF]*N
    al[0]=INF-1
    l=0
    r=N
    ok=True
    for i in range(14,0,-1):
        l2=l+fib[i]
        r2=r-fib[i]
        if query(n,l2,al)<=query(n,r2,al):
            l=l2
        else:
            r=r2
    for i in range(l,r):query(n,i,al)
    ans=INF
    for i in range(N):
        ans=max(ans,al[i])
    print('!',ans)