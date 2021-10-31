n,q=map(int, input().split())
al=list(map(int, input().split()))
ql=[int(input()) for _ in range(q)]
# ql=[(q,i) for i,q in enumerate(ql)]
# ql.sort()

al=[0]+al

c=0
cl=[0]
for i in range(n):
    d=al[i+1]-al[i]-1
    c+=d
    cl.append(c)
# print(cl)

from bisect import bisect_left, bisect_right
for q in ql:
    # print('---',q)
    cind = bisect_left(cl, q) - 1
    # print(cind)
    cnt=cl[cind]
    need=q-cnt
    aind=cind
    ans=al[aind]+need
    print(ans)

