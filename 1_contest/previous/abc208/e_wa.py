vl=[(1,1)]
vll=[vl]
for _ in range(18):
    d={}
    prev=vll[-1]
    for i in range(1,10):
        for v,c in prev:
            val=v*i
            d.setdefault(val,0)
            d[val]+=c
    vl=[]
    pat=0
    for k,v in d.items():
        vl.append((k,v))
    vl.sort()
    vll.append(vl)

vll2=[]
for vl in vll:
    new_vl=[]
    pat=0
    for k,v in vl:
        pat+=v
        new_vl.append((k,pat))
    vll2.append(new_vl)


def get_cnt(keta, val):
    if keta==0:return 1
    vl=vll2[keta]
    vn=len(vl)
    ok, ng = -1, vn+1
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if mid>=vn:
            ng=mid
            continue
        num,_=vl[mid]
        if num<=val: ok = mid
        else: ng = mid
    if ok==-1:return 0
    return vl[ok][1]

n,k=map(int, input().split())
ns=str(n)
keta=len(str(n))
ans=0

# 全桁 & 0ない
same_val=1
for i in range(len(ns)):
    ni=int(ns[i])
    if ni==0:break
    for small_num in range(1,ni):
        cval=same_val*small_num
        krem=k//cval
        if krem==0:continue
        keta_rem=len(ns)-i-1
        cnt=get_cnt(keta_rem, krem)
        ans+=cnt

    same_val*=ni
else:
    if same_val<=k:ans+=1
# print('全桁、not0',ans)


# 全桁みまん、0ない
for keta in range(1,len(ns)):
    cnt=get_cnt(keta,k)
    # print(keta,cnt)
    ans+=cnt

# print('全桁みまん、not0',ans)

# 全桁、どこかに0
dp=[[0]*4 for _ in range(len(ns)+1)]
dp[0][0]=1
n1=int(ns[0])
dp[1][0]=1
dp[1][1]=n1-1
dp[1][2]=0
dp[1][3]=0
for i in range(1,len(ns)):
    ni=int(ns[i])
    if ni==0:
        dp[i+1][0]=0
        dp[i+1][1]=dp[i][1]*9
        dp[i+1][2]=dp[i][0]+dp[i][2]
        dp[i+1][3]=dp[i][1]+dp[i][3]*10
    else:
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=dp[i][0]*(ni-1)+dp[i][1]*9
        dp[i+1][2]=0
        dp[i+1][3]=dp[i][0]+dp[i][1]+dp[i][2]*ni+dp[i][3]*10

ans+=dp[-1][3]
ans+=dp[-1][2]
# print(dp)

# 全桁未満、どこかに0
for keta in range(1,len(ns)):
    keta_rem=keta-1 # 先頭はnot0
    pat=pow(10,keta_rem)-pow(9,keta_rem)
    # print(keta,pat)
    ans+=pat*9
print(ans)