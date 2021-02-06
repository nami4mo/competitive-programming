n,k=map(int, input().split())
al=list(map(int, input().split()))
al.sort(reverse=True)
ans=0
for i in range(k):
    a=al[k-1-i]
    ans=(ans+a)/2
print(ans)