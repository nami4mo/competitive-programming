
n,k=map(int, input().split())
al=list(map(int, input().split()))

numpos=[[] for _ in range(2*10**5+1)]
for i in range(n):
    a=al[i]
    numpos[a].append(i)

from bisect import bisect_left, bisect_right

loop=0
pos=0
num=al[0]
while True:
    ind = bisect_right(numpos[num], pos)
    if ind>=len(numpos[num]):
        loop+=1
        pos=numpos[num][0]+1
        if pos==n:
            loop+=1
            break
        num=al[pos]
    else:
        pos=numpos[num][ind]+1
        if pos==n:
            loop+=1
            break
        num=al[pos]

rem=k%loop
loop=0
pos=0
num=al[0]
while True:
    if loop+1>=rem:break
    ind = bisect_right(numpos[num], pos)
    if ind>=len(numpos[num]):
        loop+=1
        pos=numpos[num][0]+1
        num=al[pos]
    else:
        pos=numpos[num][ind]+1
        num=al[pos]


from collections import deque
cnts=[0]*(2*10**5+1)
q=deque()
for a in al[pos:]:
    if cnts[a]>0:
        while q and cnts[a]>0:
            p=q.pop()
            cnts[p]-=1
    else:
        q.append(a)
        cnts[a]+=1
print(*q)