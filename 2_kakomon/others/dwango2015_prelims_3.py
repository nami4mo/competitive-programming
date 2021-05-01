def calc(bottoms,k):
    top=sum(bottoms)
    res=1
    while top>0:
        res*=top
        top-=1
        while res>1.0:
            if k>0:
                res/=3
                k-=1
            else:
                for i in range(3):
                    if bottoms[i]==0:continue
                    res/=bottoms[i]
                    bottoms[i]-=1
                    break
    for _ in range(k):
        res/=3
    for i in range(3):
        for j in range(bottoms[i]):
            res/=(j+1)
    return res

n=int(input())
dp=[-1]*(n+1)

def rec(v):
    if dp[v]!=-1:return dp[v]
    if v==1: return 0
    res=0.0
    for a in range(1,v//2+1):
        rem=v-a
        for b in range(rem+1):
            c=rem-b
            if (a>b and b>0) or (a>c and c>0):continue
            if a==b and a==c: continue
            if a==c: continue # beated by c
            prob=calc([a,b,c],v)
            res+=prob*rec(a)
    res*=3
    res+=1.0

    loop=0
    loop+=pow(1/3,v-1)
    if v%3==0:
        loop+=calc([v//3,v//3,v//3],v)
    res/=(1-loop)

    dp[v]=res
    return res

ans=rec(n)
print(ans)