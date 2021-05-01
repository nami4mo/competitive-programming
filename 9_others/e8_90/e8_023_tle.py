h,w=map(int, input().split())
cl=[list(input()) for _ in range(h)]

def rec(cnt,al,bl,res):
    if cnt==w:
        res.append((al,bl))
        return
    # if cnt>0 and (al[-1]==1 or bl[-1]==1):
    # p2=pow(2,cnt-1)
    p2=(1<<(cnt-1))
    if al>=p2 or bl>=p2:
        rec(cnt+1, al, bl, res)
    else:
        rec(cnt+1, al+p2*2, bl, res)
        rec(cnt+1, al, bl+p2*2, res)
        rec(cnt+1, al, bl, res)
    # for i in range(2):
    #     for j in range(2):
    #         if i==1 and j==1:continue
    #         if al

pairs=[]
rec(1,0,0,pairs)
rec(1,0,1,pairs)
rec(1,1,0,pairs)
# print(pairs)
# print(pairs)
# pairs.sort(key=lambda x:x[0])
# print(len(pairs))

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
    val=0
    for x in range(w):
        if cl[y][x]=='.':
            val+=(1<<x)
    # print('val',y,val)
    for u,v in pairs:
        if (val^u)&u>0:
            # print(y,u)
            continue
        new_dp[v]+=dp[u]
        new_dp[v]%=MOD
    dp=new_dp[:]
    # print(dp)


val=0
for x in range(w):
    if cl[-1][x]=='.':
        val+=(1<<x)
ans=0
for i in range(1<<w):
    if (val^i)&i>0:continue
    ans+=dp[i]
    ans%=MOD
print(ans)