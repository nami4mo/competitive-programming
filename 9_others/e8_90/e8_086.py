from itertools import product
def solve(n,ql):
    ite = list(product(range(2),repeat=n))
    res=0
    for pattern in ite:
        al=list(pattern)
        for x,y,z,w in ql:
            if (al[x]|al[y]|al[z])!=w:break
        else:
            res+=1
    return res

n,q=map(int, input().split())
ql=[]
for _ in range(q):
    x,y,z,w=map(int, input().split())
    x-=1
    y-=1
    z-=1
    ql.append((x,y,z,w))

ans=1
MOD=10**9+7
for bit in range(60):
    qll=[]
    for x,y,z,w in ql:
        if w&(1<<bit): qll.append((x,y,z,1))
        else: qll.append((x,y,z,0))
    ans*=solve(n,qll)
    ans%=MOD
print(ans)