n,m=map(int, input().split())
al=list(map(int, input().split()))
st=set(al)
k=len(st)

if m==0:
    print(k)
else:
    ans=min(n, k+m)
    print(ans)