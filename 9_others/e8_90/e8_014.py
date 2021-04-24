n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
al.sort()
bl.sort()
ans=0
for ai,bi in zip(al,bl):
    ans+=abs(ai-bi)
print(ans)