n,m=map(int, input().split())
cnts=[[0]*(m+1) for _ in range(n)]
for i in range(n):
    al=list(map(int, input().split()))
    for a in al[1:]:
        cnts[i][a]+=1

p,q=map(int, input().split())
bl=list(map(int, input().split()))
ans=0
for i in range(n):
    cnt=0
    for b in bl: cnt+=cnts[i][b]
    if cnt>=q:ans+=1
print(ans)    