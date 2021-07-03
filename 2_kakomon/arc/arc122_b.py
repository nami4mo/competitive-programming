n=int(input())
al=list(map(int, input().split()))
ave=sum(al)/n
al.sort()

csum=0
ans=10**18
for i,a in enumerate(al):
    csum+=a
    x=a/2
    xcnt=(n-1)-i
    xval=2*xcnt*x

    val=x-(csum+xval)/n
    val+=ave
    ans=min(ans,val)
    # print(x,val)
print(ans)