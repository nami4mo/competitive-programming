n=int(input())
al=list(map(int, input().split()))
d={}
for a in al:
    d.setdefault(a,0)
    d[a]+=1

ans=0
for k1,v1 in d.items():
    for k2,v2 in d.items():
        val=(k2-k1)**2
        val*=(v1*v2)
        ans+=val

ans=ans//2
print(ans)