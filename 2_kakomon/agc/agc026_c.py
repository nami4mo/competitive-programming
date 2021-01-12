n=int(input())
s=input()
sl=s[:n]
sr=s[n:]
sr=sr[::-1]

sr_cnts={}

from itertools import product
ite = list(product(range(2),repeat=n))
for pattern in ite:
    s0=[]
    s1=[]
    for i, v in enumerate(pattern):
        if v==0: s0.append(sr[i])
        if v==1: s1.append(sr[i])
    s0=''.join(s0)
    s1=''.join(s1)
    sr_cnts.setdefault((s0,s1),0)
    sr_cnts[(s0,s1)]+=1

ans=0
for pattern in ite:
    s0=[]
    s1=[]
    for i, v in enumerate(pattern):
        if v==0: s0.append(sl[i])
        if v==1: s1.append(sl[i])
    s0=''.join(s0)
    s1=''.join(s1)
    if not (s0,s1) in sr_cnts:continue
    ans+=sr_cnts[(s0,s1)]
print(ans)