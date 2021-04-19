n=int(input())
al=list(map(int, input().split()))
d={}
ans=0
for i in range(n):
    a=al[i]
    v=i-a
    d.setdefault(v,0)
    ans+=d[v]
    v2=a+i
    d.setdefault(v2,0)
    d[v2]+=1

print(ans)