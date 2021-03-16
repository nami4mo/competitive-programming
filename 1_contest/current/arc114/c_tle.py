
MOD = 998244353
n,m=map(int, input().split())

pows=[[0]*(n+1) for _ in range(m+1)]
for i in range(m+1):
    val=1
    for j in range(n+1):
        pows[i][j]=val
        val*=i
        if val>MOD:val%=MOD

ans=0
for num in range(m,0,-1):
    for cnt in range(0,n):
        numcom=pows[m-num+1][cnt]-pows[m-num][cnt]
        lowcom=(num-1)
        othercom=pows[m][n-cnt-1]
        pat=numcom*lowcom*othercom*2
        ans+=pat

        if cnt!=n-1:
            # numcom=pow(m-num+1,cnt)-pow(m-num,cnt)
            lowcom=(num-1)*(num-1)
            othercom=pows[m][n-cnt-2]
            pat=numcom*lowcom*othercom*(n-cnt-2+1)
            ans+=pat
        if ans>MOD: ans%=MOD
    
    ans+=pows[m-num+1][n]
    ans-=pows[m-num][n]

print(ans%MOD)