n,k=map(int, input().split())
vl=[0,1]
for _ in range(20):
    st=set()
    for i in range(1,10):
        for v in vl:
            val=v*i
            if val<=k:st.add(val)
    vl=list(st)

INF=k+1
vl.sort()
vl.append(INF)
vlen=len(vl)
v2i={}
for i,v in enumerate(vl):
    v2i[v]=i

ns=str(n)
nl=len(ns)
dp_same=[[0]*vlen for _ in range(nl+1)]
dp_small=[[0]*vlen for _ in range(nl+1)]
dp_same[0][v2i[1]]=1

for i in range(nl):
    ni=int(ns[i])
    for j in range(vlen):
        val=vl[j]*ni
        if val>k:val=INF
        dp_same[i+1][v2i[val]]+=dp_same[i][j]
        for num in range(10):
            if i==0 and num==0:continue
            val=vl[j]*num
            if val>k:val=INF
            if num<ni:
                dp_small[i+1][v2i[val]]+=dp_same[i][j]
            dp_small[i+1][v2i[val]]+=dp_small[i][j]

ans=sum(dp_small[-1][:-1])+sum(dp_same[-1][:-1])

for keta in range(1,nl):
    dp=[[0]*vlen for _ in range(keta+1)]
    dp[0][v2i[1]]=1
    for i in range(keta):
        for j in range(vlen):
            for num in range(10):
                if i==0 and num==0:continue
                val=vl[j]*num
                if val>k:val=INF
                dp[i+1][v2i[val]]+=dp[i][j]
    ans+=sum(dp[keta][:-1])
print(ans)