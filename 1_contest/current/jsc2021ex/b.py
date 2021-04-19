n,m=map(int, input().split())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
cnts=[0]*(10**4)

for a in al:
    cnts[a]+=1
for b in bl:
    cnts[b]+=1

ans=[]
for i in range(10**4):
    if cnts[i]==1:
        ans.append(i)
print(*ans)