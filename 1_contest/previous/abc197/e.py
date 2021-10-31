n=int(input())

INF=10**10
cmins=[INF]*(n)
cmaxs=[-INF]*(n)
for _ in range(n):
    x,c=map(int, input().split())
    c-=1
    cmins[c]=min(cmins[c],x)
    cmaxs[c]=max(cmaxs[c],x)

# print(cmins)
# print(cmaxs)

dp_l=0
dp_r=0
lpos=0
rpos=0
for c in range(n):
    if cmins[c]==INF:continue
    v1=abs(lpos-cmaxs[c])+abs(cmaxs[c]-cmins[c])
    v2=abs(rpos-cmaxs[c])+abs(cmaxs[c]-cmins[c])

    v3=abs(lpos-cmins[c])+abs(cmaxs[c]-cmins[c])
    v4=abs(rpos-cmins[c])+abs(cmaxs[c]-cmins[c])
    dp_l, dp_r = min(dp_l+v1, dp_r+v2), min(dp_l+v3, dp_r+v4)
    lpos=cmins[c]
    rpos=cmaxs[c]

ans1=dp_l+abs(lpos)
ans2=dp_r+abs(rpos)
ans=min(ans1,ans2)
print(ans)