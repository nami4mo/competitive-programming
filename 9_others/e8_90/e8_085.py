n=int(input())
ans=0
for a in range(1,10**4+1):
    if n%a!=0:continue
    d=n//a
    for b in range(a,10**6+1):
        if d%b!=0:continue
        c=d//b
        if b>c:break
        ans+=1
print(ans)