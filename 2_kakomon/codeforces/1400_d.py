def com4(v):
    val=v*(v-1)*(v-2)*(v-3)//24
    return val

ansl=[]
for _ in range(int(input())):
    n=int(input())
    al=list(map(int, input().split()))
    
    ans=0
    dp=[[0]*(n+1) for _ in range(n+1)]
    dcnt=[0]*(n+1)
    for i in range(n):
        a=al[i]
        dcnt[a]+=1
        acnt=0
        for j in range(i):
            if al[j]==a:acnt+=1
            else:
                dp[a][al[j]]+=acnt
        for j in range(n+1):
            if a!=j:ans+=dp[j][al[i]]
    for i in range(n+1):
        if dcnt[i]>=4:
            ans+=com4(dcnt[i])
    ansl.append(ans)

for a in ansl:print(a)