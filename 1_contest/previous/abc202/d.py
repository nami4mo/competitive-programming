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
# MOD = 10**9+7
comb = Combination(100,10**18+3)
# comb.com(10,3)

a,b,k=map(int, input().split())
# dp=[[0]*(b+1) for _ in range(a+1)]

# for i in range(a+1):
#     for j in range(b+1):

# for k in range(1,20):

cnt=0
arem=a
brem=b
n=a+b
ans=[]
for i in range(n):
    use_a=comb.com(arem-1+brem,brem)
    if arem<=0:
        ans.append('b')
        continue
    elif brem<=0:
        ans.append('a')
        continue

    if cnt+use_a>=k:
        arem-=1
        ans.append('a')
        # cnt+=use_a
    else:
        brem-=1
        cnt+=use_a
        ans.append('b')
    # print(cnt,ans)
ans=''.join(ans)
print(ans)