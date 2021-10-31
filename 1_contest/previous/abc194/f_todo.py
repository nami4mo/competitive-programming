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

MOD=10**9+7
comb = Combination(10**2, MOD)
# comb.com(10,3)

d={}
for i in range(10):
    d[str(i)]=i
d['A']=10
d['B']=11
d['C']=12
d['D']=13
d['E']=14
d['F']=15

n,k=map(str, input().split())
k=int(k)
nl=len(n)

ans=0
dp_sm=[0]*(nl+1)
dp_sa=[0]*(nl+1)
# dp_sa[0]=st
dp_st=set()
for i in range(nl-1):
    if d[n[i]]==0:continue

    alreadys=[]
    for v in list(dp_st):
        if d[n[i]]<d[n[i]]:
            alreadys.append(v)

    already=len(dp_st)
    if already>k:continue
    pat=len(alreadys)
    rem=k-already
    tail=nl-i-1
    val=0
    plus=True
    for i in range(k,0,-1):
        if plus:
            val+=pow(i,tail,MOD)*comb.com(16-already,i-already)
        else:
            val-=pow(i,tail,MOD)*comb.com(16-already,i-already)
        val%=MOD
        plus=not plus
    ans+=val*pat
    ans%=MOD

    already=len(dp_st)+1
    if already>k:continue
    pat=len(dp_st)-len(alreadys)
    rem=k-already
    tail=nl-i-1
    val=0
    plus=True
    for i in range(k,0,-1):
        if plus:
            val+=pow(i,tail,MOD)*comb.com(16-already,i-already)
        else:
            val-=pow(i,tail,MOD)*comb.com(16-already,i-already)
        val%=MOD
        plus=not plus
    ans+=val*pat
    ans%=MOD

    dp_st.add(n[i])


print(ans)
for free_len in range(1,nl):
    val=0
    plus=True
    for i in range(k,0,-1):
        if plus:
            val+=pow(i,free_len,MOD)*comb.com(16,i)*comb._finv[i]
        else:
            val-=pow(i,free_len,MOD)*comb.com(16,i)*comb._finv[i]
        val%=MOD
        plus=not plus
    ans+=val
    print('--',free_len,val)


# ans-=1
ans%=MOD
print(ans)