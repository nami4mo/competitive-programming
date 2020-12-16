n=int(input())
d={}
for _ in range(n):
    a=int(input())
    if a not in d: d[a]=0
    d[a]+=1

ans=0
for v in d.values():
    if v%2==1: ans+=1

print(ans)