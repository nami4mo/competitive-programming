from bisect import bisect_left, bisect_right

n=int(input())
dl=[int(input()) for _ in range(n)]
dl.sort()

c2=[]
for i in range(n):
    cnt = bisect_right(dl, dl[i]//2)
    c2.append(cnt)

c2cs=[0]
cs=0
for c in c2:
    cs+=c
    c2cs.append(cs)

ans=0
for i in range(2,n-1):
    ind = bisect_right(dl, dl[i]//2)
    ans+=c2cs[ind]*(n-bisect_left(dl, dl[i]*2))
    ans%=(10**9+7)
print(ans)
