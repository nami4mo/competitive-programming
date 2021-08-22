N_MAX = 10**6
MOD = 10**9 + 7
fac, finv, inv = [0]*N_MAX ,[0]*N_MAX, [0]*N_MAX
def com_init():
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2, N_MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

def com(n, k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


n,k = map(int, input().split())
al = list(map(int, input().split()))
com_init()
al.sort()

ans_max = 0
ans_min = 0
for i,a in enumerate(al):
    ans_max += a*com(i,k-1)
    ans_max%=MOD
    ans_min += a*com(n-1-i,k-1)
    ans_min%=MOD


print((ans_max-ans_min)%MOD)