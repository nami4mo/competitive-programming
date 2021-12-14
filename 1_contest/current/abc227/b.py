n=int(input())
sl=list(map(int, input().split()))

ans=0
for s in sl:
    ok=False
    for a in range(1,500):
        for b in range(1,500):
            if 4*a*b+3*a+3*b==s:ok=True
    if ok:ans+=1
print(n-ans)