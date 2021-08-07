def p_factorization_t(n):
    if n == 1: return []
    pf_cnt = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            pf_cnt.append((i,cnt))

    if temp != 1: pf_cnt.append((temp,1))
    return pf_cnt

from math import gcd
def lcm(a,b):
    return (a*b)//gcd(a,b)

n=int(input())
abl=[]
ablp=[]
for _ in range(n):
    a,b=map(int, input().split())
    abl.append((a,b))

d={}
ps_a=p_factorization_t(abl[0][0])
ps_b=p_factorization_t(abl[0][1])
for p,c in ps_a:
    d[p]=c
for p,c in ps_b:
    d.setdefault(p,c)
    d[p]=max(d[p],c)

# ablp.append((ps_a,ps_b))

for a,b in abl[1:]:
    ps_a=p_factorization_t(a)
    ps_b=p_factorization_t(b)
    dd={}
    for p,c in ps_a:
        dd[p]=c
    for p,c in ps_b:
        dd.setdefault(p,c)
        dd[p]=max(dd[p],c)
    new_d={}
    for p,c in d.items():
        if p not in dd:continue
        new_d[p]=min(dd[p],d[p])
    d=new_d.copy()
    # ablp.append((ps_a,ps_b))

# print(d)
ps=[]
for p,c in d.items():
    ps.append((p,c))
ps.sort()
primes=[]
cnts=[]
for p,c in ps:
    primes.append(p)
    cnts.append(c)

pn=len(ps)
c_cnts=[0]*pn
cnts_lr=[]
# print(primes,cnts)
ans=1
def dfs(depth):
    global ans
    if depth==pn:
        left=1
        right=1
        for i in range(pn):
            p=primes[i]
            lc,rc=cnts_lr[i]
            left*=pow(p,lc)
            right*=pow(p,rc)
        for a,b in abl:
            if not ((a%left==0 and b%right==0) or (a%right==0 and b%left==0)):break
        else:
            # print(left,right)
            val=lcm(left,right)
            ans=max(ans,val)
        return
    cmax=cnts[depth]
    for i in range(cmax+1):
        for j in range(cmax+1):
            cnts_lr.append((i,j))
            dfs(depth+1)
            cnts_lr.pop()

dfs(0)
print(ans)
