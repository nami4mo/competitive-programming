def s2t(s):
    h,m=s.split(':')
    res=60*int(h)+int(m)
    return res

def check(ses):
    ok=True
    t=0
    for s,e in ses:
        if t>s:return False
        t=e
    for s,e in ses:
        s+=1440
        e+=1440
        if t>s:return False
        t=e
    return True


n=int(input())
ans=0
sel=[]
for _ in range(n):
    s,e=map(str, input().split())
    s,e=s2t(s),s2t(e)
    sel.append((s,e))

sel.sort()
INF=100
dp=[INF]*(1<<n)
for i in range(1<<n):
    ses=[]
    for bit in range(n):
        if i&(1<<bit)>0: ses.append(sel[bit])
    if check(ses):dp[i]=1
# print(dp)
for i in range(1<<n):
    bits=(i-1)&i
    while bits>0:
        bits=(bits-1)&i
        if bits==0:break
        comp=bits^i
        dp[i]=min(dp[i],dp[bits]+dp[comp])
# print(dp)
print(dp[-1])