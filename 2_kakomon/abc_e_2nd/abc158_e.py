n,p=map(int, input().split())
s=input()

if p==2 or p==5:
    ans=0
    for i in range(n):
        si=int(s[n-i-1])
        if si%p==0:
            ans+=(n-i)
    print(ans)
    exit()


rems=[0]*p
rems[0]=1
ans=0
tens=1
v=0
for i in range(n):
    si=int(s[n-i-1])
    v+=tens*si
    v%=p
    ans+=rems[v]
    rems[v]+=1
    tens*=10
    tens%=p
print(ans)