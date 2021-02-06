n=int(input())
al=list(map(int, input().split()))

ans=-10**18
for i in range(n):
    aoki_max=-10**18
    tak=0
    for j in range(n):
        av=0
        tv=0
        if i==j:continue
        if j<i:
            for k in range(j,i+1):
                if (j-k)%2==0:tv+=al[k]
                else: av+=al[k]
        else:
            for k in range(i,j+1):
                if (i-k)%2==0:tv+=al[k]
                else: av+=al[k]
        if av>aoki_max:
            aoki_max=av
            tak=tv
    ans=max(ans,tak)

print(ans)