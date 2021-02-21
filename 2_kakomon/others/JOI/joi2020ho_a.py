n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))

ansl=[-1]*(n+1)
ans=0
for i in range(n):
    ans=max(al[i+1]-bl[i],0,ans)
ansl[0]=ans

for i in range(1,n+1):
    poped=max(al[i]-bl[i-1],0)
    inserted=max(al[i-1]-bl[i-1],0)
    ans-=poped
    ans+=inserted
    ansl[i]=ans
print(*ansl)