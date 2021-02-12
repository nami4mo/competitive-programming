n=int(input())
al=[-1]+list(map(int, input().split()))
ans=0
for i in range(n+1):
    like=al[i]
    if al[like]==i:ans+=1
print(ans//2)