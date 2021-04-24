n,m=map(int, input().split())

ww=[[] for _ in range(n)]
wr=[[] for _ in range(n)]

for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    ww[a].append(b)
    wr[b].append(a)

s=input().rstrip()
from collections import deque
sq=deque(list(s))
res=[]
cands=[]
while sq:
    # print(sq)
    if sq[0]=='"' and sq[-1]=='w':
        res.append('w')
        sq.popleft()
        for _ in range(3): sq.pop()
    elif sq[0]=='"' and sq[-1]=='"':
        res.append('n')
        sq.popleft()
        sq.pop()
    else:
        for _ in range(5):sq.popleft()
        if sq[-1]=='w':
            sq.pop()
            ss=''
            while sq:ss+=sq.popleft()
            t=int(ss)-1
            cands=wr[t][:]
            break
        else:
            ss=''
            while sq:ss+=sq.popleft()
            t=int(ss)-1
            cands=[]
            for v in range(n):
                ok=True
                for target in ww[v]:
                    if target==t:ok=False
                if ok:cands.append(v)
            break
# print(cands)
res=res[::-1]
# print(res)
for r in res:
    new_cands=[]
    cnts=[0]*n
    for c in cands:
        for aite in wr[c]:
            cnts[aite]+=1
    if r=='n':
        ccnt=len(cands)
        for i in range(n):
            if cnts[i]<ccnt:new_cands.append(i)
    else:
        for i in range(n):
            if cnts[i]>=1:new_cands.append(i)
    cands=new_cands[:]
print(len(cands))