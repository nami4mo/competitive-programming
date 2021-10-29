n,p=map(int, input().split())
al=list(map(int, input().split()))
ans=0
for a in al:
    if a<p:ans+=1
print(ans)