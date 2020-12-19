n=int(input())
al=list(map(int, input().split()))
al.sort()

csum=sum(al)
ans=0
for i in range(n):
    a=al[i]
    csum -= a
    val = csum-a*(n-i-1)
    ans+=val

print(ans)