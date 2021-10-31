n=int(input())
ans=0
for i in range(1,10**6+1):
    s=str(i)
    ss=int(s+s)
    if 1<=ss<=n: ans+=1
print(ans)