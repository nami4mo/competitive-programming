k,n=map(int, input().split())
vwl=[]
for _ in range(n):
    v,w=map(str, input().split())
    vwl.append((v,w))


from itertools import product
ite = list(product(range(3),repeat=k))
for pattern in ite:
    pattern = list(pattern)
    ok=True
    for v,w in vwl:
        cnt=0
        for vi in v:
            cnt+=(pattern[int(vi)-1]+1)
        if cnt!=len(w):
            ok=False
    if ok:
        ansl=['.']*k
        for v,w in vwl:
            pos=0
            for vi in v:
                vlen=pattern[int(vi)-1]+1
                ansl[int(vi)-1]=w[pos:pos+vlen]
                pos+=vlen
        for ans in ansl:print(ans) 
        break