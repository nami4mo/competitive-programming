from collections import deque

n=int(input())
al=list(map(int, input().split()))
cnts={}
for a in al:
    cnts.setdefault(a,0)
    cnts[a]+=1

cl=list(cnts.values())
cl.sort()
cq=deque(cl)

xsums=[0]
csum=0
for x in range(1,n+1):
    while cq and cq[0]<x:
        cq.popleft()
    csum+=len(cq)
    xsums.append(csum)

ansl=[]
# print(xsums)
for k in range(1,n+1):
    ok, ng = 0, 3*10**6
    while abs(ok-ng) > 1:
        x = (ok+ng)//2
        ok_flag = True
        if x<len(xsums) and x*k<=xsums[x]:
            ok = x
        else:
            ng = x
    ansl.append(ok)
for a in ansl: print(a)