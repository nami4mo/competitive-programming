n=int(input())
al=list(map(int, input().split()))

d={0:1}
v=0
ans=0
for i,a in enumerate(al):
    if i%2==0: v+=a
    else: v-=a
    d.setdefault(v,0)
    ans+=d[v]
    d[v]+=1
print(ans)
