n=int(input())
al=[]
bl=[]
for _ in range(n):
    a,b=map(int, input().split())
    al.append(a)
    bl.append(b)

ans=10**10
for i in range(n):
    for j in range(n):
        if i==j:
            v=al[i]+bl[j]
        else:
            v=max(al[i],bl[j])
        ans=min(ans,v)
print(ans)