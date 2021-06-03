from bisect import bisect_left, bisect_right

n,d,k=map(int, input().split())
psl=[]
st=set()
for _ in range(n):
    p,s=map(int, input().split())
    psl.append((p,s))
    st.add(s)
psl.sort(key=lambda x:x[1])

sl=list(st)
sl.sort()
i2s=[0]
s2i={}
for i in range(len(sl)):
    i2s.append(sl[i])
    s2i[sl[i]]=i+1

next1s={}
next2s={}
prev1=0
prev2=0
sl1=[]
sl2=[]
for i in range(n):
    p,s=psl[i]
    psl[i]=(p,s2i[s])
    if p==1:
        next1s[prev1]=s2i[s]
        prev1=s2i[s]
        sl1.append(s)
    else:
        next2s[prev2]=s2i[s]
        prev2=s2i[s]
        sl2.append(s)

dp1=[0]*(len(sl)+1)
dp2=[0]*(len(sl)+1)

if next1s: dp1[min(list(next1s.values()))]=1
if next2s: dp2[min(list(next2s.values()))]=1

for p,s in psl:
    if p==1:
        if s in next1s:
            neib_s=next1s[s]
            dp1[neib_s]=max(dp1[neib_s],dp1[s]+1)
        j=dp1[s]
        t=i2s[s]+d+k*j+1
        ind = bisect_left(sl2, t)
        if ind==len(sl2):continue
        next_s=sl2[ind]
        next_si=s2i[next_s]
        dp2[next_si]=max(dp2[next_si],dp1[s]+1)
    else:
        if s in next2s:
            neib_s=next2s[s]
            dp2[neib_s]=max(dp2[neib_s],dp2[s]+1)
        j=dp2[s]
        t=i2s[s]+d+k*j+1
        ind = bisect_left(sl1, t)
        if ind==len(sl1):continue
        next_s=sl1[ind]
        next_si=s2i[next_s]
        dp1[next_si]=max(dp1[next_si],dp2[s]+1)

ans=max(max(dp1),max(dp2))
print(ans)