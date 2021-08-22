n,k=map(str, input().split())
k=int(k)
nl=len(n)

d={}
for i in range(10):
    d[str(i)]=i
d['A']=10
d['B']=11
d['C']=12
d['D']=13
d['E']=14
d['F']=15

MOD=10**9+7
dp=[[0]*18 for _ in range(nl+1)]
dp[1][1]=d[n[0]]-1
st=set()
st.add(d[n[0]])
for i in range(1,nl):
    si=d[n[i]]
    for j in range(17):
        dp[i+1][j]+=dp[i][j]*j
        if j+1<=16: 
            dp[i+1][j+1]+=dp[i][j]*(16-j)

    # if i>0:
    dp[i+1][1]+=15
    # if si==0:continue

    alre=len(st)
    small_cnt=0
    for num in list(st):
        if num<si: small_cnt+=1
    not_exist_cnt=si-small_cnt
    # print(small_cnt,not_exist_cnt,alre)
    dp[i+1][alre]+=small_cnt
    dp[i+1][alre+1]+=max(not_exist_cnt,0)
    for j in range(17):
        dp[i+1][j]%=MOD
    st.add(si)

# print(dp)
ans=dp[nl][k]
if len(st)==k:ans+=1
print(ans%MOD)