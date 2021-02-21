n,m=map(int, input().split())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
al.sort()
bl.sort()

ae=[False]*(n*m+1)
be=[False]*(n*m+1)
for a in al: 
    if ae[a]:
        print(0)
        exit()
    ae[a]=True
for b in bl: 
    if be[b]:
        print(0)
        exit()
    be[b]=True

from bisect import bisect_left, bisect_right

ans=1
MOD=10**9+7
for i in range(n*m,0,-1):
    if ae[i] and be[i]:continue
    elif ae[i]:
        cnt = m-bisect_left(bl, i)
        ans*=cnt
    elif be[i]:
        cnt = n-bisect_left(al, i)
        ans*=cnt
    else:
        cnt1 = m-bisect_left(bl, i)
        cnt2 = n-bisect_left(al, i)
        cnt=cnt1*cnt2-((n*m)-i)
        ans*=cnt
    ans%=MOD
print(ans)
        