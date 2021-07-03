n=int(input())
al=list(map(int, input().split()))
d={}
for a in al:
    d.setdefault(a,0)
    d[a]+=1

no=0
for k,v in d.items():
    val=v*(v-1)//2
    no+=val

ans=n*(n-1)//2 -no
print(ans)