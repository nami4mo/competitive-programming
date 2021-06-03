n=int(input())
al=list(map(int, input().split()))
ma=al[0]
last=al[0]*2
ans=al[0]*2
print(ans)

for i in range(1,n):
    if ma>=al[i]:
        last=al[i]+last
        ans+=last
    else:
        d=al[i]-ma
        ans+=(i*d)
        last=last+d+al[i]
        ans+=last
        ma=al[i]
    print(ans)