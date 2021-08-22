# TLE! rewrite with C++
import sys
sys.setrecursionlimit(10**6)

def modinv(a,m):
    b, u, v = m, 1, 0
    while b:
        t = a//b
        a -= t*b
        a,b = b,a
        u -= t * v
        u,v = v,u
    u %= m
    return u

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

    def finv(self,r):
        return self._finv[r]

MOD = 10**9+7
comb = Combination(10**6, MOD)


def dfs1(pare, node, gl, dp):
    node_v = 1
    node_size = 1
    sizes = []
    for neib in gl[node]:
        if pare==neib: continue
        child_v, child_size = dfs1(node, neib, gl, dp)
        node_v *= child_v
        node_v%=MOD
        node_size += child_size
        sizes.append(child_size)
    node_v *= comb.fac(node_size-1)
    for v in sizes:
        node_v *= comb.finv(v)
        node_v%=MOD
    dp[node] = (node_v, node_size)
    return node_v, node_size


def dfs2(pare, node, pare_v, pare_size, gl, dp, ansl):
    node_v, node_size = dp[node]
    node_v *= comb.perm(node_size-1+pare_size,pare_size)
    node_v *= comb.finv(pare_size)
    node_v *= pare_v
    node_size += pare_size
    ansl[node] = node_v%MOD

    for neib in gl[node]:
        if pare==neib: continue
        child_v, child_size = dp[neib]
        new_node_v = node_v
        new_node_v *= modinv(comb.perm(node_size-1,child_size),MOD)
        new_node_v *= comb.fac(child_size)
        new_node_v *= modinv(child_v,MOD)
        new_node_v %= MOD
        new_node_size = node_size-child_size
        dfs2(node, neib, new_node_v, new_node_size, gl, dp, ansl)


n=int(input())
gl=[[] for _ in range(n)]
dp = [(-1,-1)]*n
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

dfs1(-1,0,gl,dp)
# print(dp)
ansl = [-1]*n
dfs2(-1,0,1,0,gl,dp,ansl)
for a in ansl:
    print(a)