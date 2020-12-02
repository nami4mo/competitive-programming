n,k=map(int, input().split())
al=list(map(int, input().split()))
cumsums=[0]
c=0
for a in al:
    c+=a
    cumsums.append(c)

sums=[]
for l in range(n):
    for r in range(l+1,n+1):
        v=cumsums[r]-cumsums[l]
        sums.append(v)

# cands = []
ans = 0
for powk in range(40,-1,-1):
    tmp_cands=[]
    for v in sums:
        if (v>>powk)%2==1:
            tmp_cands.append(v)
    if len(tmp_cands)>=k:
        # cands=tmp_cands[:]
        sums=tmp_cands[:]
        ans+=(2**powk)

print(ans)