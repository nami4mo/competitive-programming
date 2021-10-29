n,k=map(int, input().split())
cl=list(map(int, input().split()))
pl=list(map(int, input().split()))
d={}
for c,p in zip(cl,pl):
    d.setdefault(c,p)
    d[c]=min(d[c],p)
dl=list(d.values())
dl.sort()
if len(dl)<k:print(-1)
else:print(sum(dl[:k]))