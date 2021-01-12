n,prime=map(int, input().split())
abcl=[]
for i in range(n):
    a,b,c=map(int, input().split())
    abcl.append((a,b,c))

abcl.sort()
imos={}
for a,b,c in abcl:
    imos.setdefault(a,0)
    imos.setdefault(b+1,0)
    imos[a]+=c
    imos[b+1]-=c

ans=0
imos=list(imos.items())
imos.sort(key=lambda x: x[0])
prev_t, curr_v=imos[0]
for t,v in imos[1:]:
    d = t-prev_t
    ans+=min(prime, curr_v)*d
    prev_t=t
    curr_v+=v
print(ans)