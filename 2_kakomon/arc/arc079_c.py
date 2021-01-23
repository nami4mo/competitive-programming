n=int(input())
al=list(map(int, input().split()))

ans=0
while True:
    al.sort(reverse=True)
    if al[0]<=n-1:break
    dist=al[0]-(n-1)
    cnt=(dist-1)//n+1
    ans+=cnt
    al[0]-=cnt*n
    for i in range(1,n):
        al[i]+=cnt
print(ans)