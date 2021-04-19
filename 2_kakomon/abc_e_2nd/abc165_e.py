n,m=map(int, input().split())
if n%2==1:
    for i in range(m):
        d=(n-1)-i*2
        l=i
        r=l+d
        print(l+1,r+1)
else:
    for i in range(m):
        d=n//2-1-i
        l=(i//2)
        r=l+d
        if i%2==1:
            l+=(n//2)
            r+=(n//2)
        print(l+1,r+1)