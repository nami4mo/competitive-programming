n,r=map(int, input().split())
s=input()
cnt=0
far=0
skip=0
for i in range(n-1,-1,-1):
    if skip>0:skip-=1
    else:
        if s[i]=='o':pass
        else:
            cnt+=1
            shot=i-r+1
            skip=r-1
            far=max(far,shot)
ans=cnt+far
print(ans)