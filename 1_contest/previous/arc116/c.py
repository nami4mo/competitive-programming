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
MOD=998244353
comb = Combination(3*10**5, MOD)
# comb.com(10,3)


n,m=map(int, input().split())

dp=[[0]*(m+1) for _ in range(21)]
dp[0][1]=1
for i in range(1,m+1):
    dp[0][i]=1
for i in range(20):
    for j in range(1,m+1):
        for k in range(2,1000000):
            bai=j*k
            if bai>m:break
            dp[i+1][bai]+=dp[i][j]

# print(dp[:4])
# for i in range(4):
#     print(dp[i])
ans=0
used=[False]*(m+1)
for i in range(20,-1,-1):
    for j in range(m,-1,-1):
        if dp[i][j]!=0:
            used[j]=True
            rem=n-(i+1)
            pat=comb.com(rem+i,i)*dp[i][j]
            ans+=pat
            ans%=MOD
            # print(i,j,pat)

print(ans)
            