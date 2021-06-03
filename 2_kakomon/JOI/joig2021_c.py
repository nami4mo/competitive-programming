n=int(input())
al=list(map(int, input().split()))
ll,rl=[0],[0]
off=0
ans=10**10
for i,a in enumerate(al):
    if a==0:off+=1
    ll.append(off)

on=0
for i in range(n-1,-1,-1):
    if al[i]==1:on+=1
    rl.append(on)

for i in range(n+1):
    ans=min(ans, ll[i]+rl[n-i])
print(ans)