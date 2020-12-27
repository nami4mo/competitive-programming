a,b,c=map(int, input().split())
ans=0
ca=min(a,c)
ans+=ca
c-=ca
if c<=b+1:
    ans+=b
    ans+=c
else:
    ans+=(b+1)
    ans+=b
print(ans)