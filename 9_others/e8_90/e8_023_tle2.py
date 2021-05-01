h,w=map(int, input().split())
cl=[list(input()) for _ in range(h)]

okis=[]
for i in range(1<<w):
    for j in range(w-1):
        if (i&(1<<j)) and (i&(1<<j+1)):break
    else:
        okis.append(i)


dp=[0]*(1<<w)
for i in range(1<<w):
    ok=True
    last=-2
    for j in range(w):
        if i&(1<<j)==0:continue
        if cl[0][j]=='#' or last+1==j:
            ok=False
            break
        last=j
    if ok:dp[i]=1

MOD=10**9+7
for y in range(h-1):
    new_dp=[0]*(1<<w)
    # for i in range(1<<w):
    for i in okis:
        oks=[True]*w
        for j in range(w):
            if cl[y+1][j]=='#':oks[j]=False
            if i&(1<<j)==0:continue
            if j-1>=0:oks[j-1]=False
            oks[j]=False
            if j+1<w:oks[j+1]=False
        bits=0
        # print(oks)

        for j in range(w):
            if oks[j]:bits+=(1<<j)

        # for j 

        for oki in okis:
            if (bits^oki)&oki==0:
                # print(bits,oki)
                new_dp[oki]+=dp[i]
                new_dp[bits]%=MOD
        # print()
        # new_dp[bits]+=dp[i]
        # new_dp[bits]%=MOD
    # for j in range(w):
    #     bit=1<<j
    #     for i in range(1<<w):
    #         if i&bit==0:
    #             new_dp[i]+=new_dp[i|bit]
    #             new_dp[bits]%=MOD
    dp=new_dp[:]

ans=0
for i in okis:
    ans+=dp[i]
    ans%=MOD
print(ans)