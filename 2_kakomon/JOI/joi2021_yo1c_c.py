n,m=map(int, input().split())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
ans=0
for i in range(n):
    for j in range(m):
        if al[i]<=bl[j]:ans+=1
print(ans)