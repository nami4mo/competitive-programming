n,p,q=map(int, input().split())
al=list(map(int, input().split()))

n=100
al=list(range(10**8,10**8+n))


ans=0
for i1 in range(0,n-4):
    v1=al[i1]
    for i2 in range(i1+1,n-3):
        v2=al[i2]*v1
        v2%=p
        for i3 in range(i2+1,n-2):
            v3=al[i3]*v2
            v3%=p
            for i4 in range(i3+1,n-1):
                v4=al[i4]*v3
                v4%=p
                for i5 in range(i4+1,n):
                    v5=al[i5]*v4
                    if v5%p==q:ans+=1
print(ans)