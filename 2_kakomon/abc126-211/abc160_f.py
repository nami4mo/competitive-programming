from collections import deque
def make_order_parents(n,gl,root=0):
    order=[root]
    parents=[-1]*n
    q=deque([root])
    while q:
        poped=q.popleft()
        for neib in gl[poped]:
            if parents[neib]!=-1 or neib==root:continue
            parents[neib]=poped
            order.append(neib)
            q.append(neib)
    return order,parents

class Combination:
    def __init__(self, n_max=10**6, mod=10**9+7):
        # self._n_max = n_max
        self._fac, self._finv, self._inv = [0]*n_max, [0]*n_max, [0]*n_max
        self._fac[0], self._fac[1] = 1, 1
        self._finv[0], self._finv[1] = 1, 1
        self._inv[1] = 1
        self._mod = mod
        for i in range(2, n_max):
            self._fac[i] = self._fac[i - 1] * i % self._mod
            self._inv[i] = self._mod - self._inv[self._mod%i] * (self._mod // i) % self._mod
            self._finv[i] = self._finv[i - 1] * self._inv[i] % self._mod
    def com(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self._fac[n] * (self._finv[r] * self._finv[n - r] % self._mod) % self._mod

    def perm(self,n,r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self._fac[n] * (self._finv[n-r] % self._mod) % self._mod

    def fac(self,n):
        return self._fac[n]

    def finv(self,n):
        return self._finv[n]

MOD = 10**9+7
comb = Combination(2*10**5+10, MOD)

n=int(input())
gl=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)
order,pare=make_order_parents(n,gl)

dp_cnt=[0]*n
dp_pat=[1]*n
for v in order[::-1]:
    dp_pat[v]*=comb.fac(dp_cnt[v])
    dp_pat[v]%=MOD
    dp_cnt[v]+=1

    cpare = pare[v]
    if cpare==-1:continue
    dp_cnt[cpare]+=dp_cnt[v]
    dp_pat[cpare]*=dp_pat[v]
    dp_pat[cpare]*=comb.finv(dp_cnt[v])
    dp_pat[cpare]%=MOD


q=deque([0])
passl=[(0,1)]*n
ansl=[-1]*n
ansl[0]=dp_pat[0]

## あえて累積を使う方法で解く
while q:
    poped=q.popleft()

    # left/right cumsum
    cntl,cntr=[0],[0]
    finvl,finvr=[1],[1]
    patl,patr=[1],[1]

    cnts,pats=[],[]
    for neib in gl[poped]:
        if ansl[neib]!=-1:continue
        cnts.append(dp_cnt[neib])
        pats.append(dp_pat[neib])
    for c in cnts:
        cntl.append(cntl[-1]+c)
        finvl.append(finvl[-1]*comb.finv(c)%MOD)
    for c in cnts[::-1]:
        cntr.append(cntr[-1]+c)
        finvr.append(finvr[-1]*comb.finv(c)%MOD)
    for c in pats: patl.append(patl[-1]*c%MOD)
    for c in pats[::-1]: patr.append(patr[-1]*c%MOD)

    childnum=len(gl[poped])-1
    if poped==0:childnum+=1
    pare_cnt,pare_pat=passl[poped]

    # calc answer from "all children" and "parent"
    ans=comb.fac(cntl[childnum]+pare_cnt)*patl[childnum]*pare_pat*finvl[childnum]*comb.finv(pare_cnt)
    ansl[poped]=ans%MOD

    # send info (from parent + the other children) to each child
    cind=0
    for neib in gl[poped]:
        if ansl[neib]!=-1:continue
        rind=childnum-cind-1
        cnt=cntl[cind]+cntr[rind]+pare_cnt
        pat=patl[cind]*patr[rind]*pare_pat*comb.fac(cnt)*comb.finv(pare_cnt)*finvl[cind]*finvr[rind]
        q.append(neib)
        passl[neib]=(cnt+1,pat%MOD)
        cind+=1

# print(ansl)
for a in ansl:print(a)