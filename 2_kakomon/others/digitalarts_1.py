s=input()
sl=s.split()

n=int(input())
ngs=[]
for _ in range(n):
    ng=input()
    ngs.append(ng)

ansl=[]
for si in sl:
    ok=True
    for ng in ngs:
        same=True
        if len(si)!=len(ng):continue
        for i in range(len(si)):
            if si[i]!=ng[i] and ng[i]!='*': same=False
        if same:ok=False
    if ok: ansl.append(si)
    else: ansl.append('*'*len(si))
print(' '.join(ansl))