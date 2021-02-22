n,q,k=map(int, input().split())
al=[0]+list(map(int, input().split()))+[k]
cs=0
csums=[0]
for i in range(1,n+1):
    pattern=al[i+1]-al[i]+al[i]-al[i-1]-2
    pattern=max(pattern,0)
    cs+=pattern
    csums.append(cs)

# print(csums)
ansl=[]
for _ in range(q):
    l,r=map(int, input().split())
    # l-=1
    # r-=1
    ans=csums[r-1]-csums[l]
    ladd=al[l+1]-al[l]-1+al[l]-1
    radd=k-al[r]+al[r]-al[r-1]-1
    ans+=(ladd+radd)
    ansl.append(ans)

for a in ansl:print(a)
