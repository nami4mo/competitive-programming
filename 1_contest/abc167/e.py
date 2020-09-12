N_MAX = 10**6
MOD = 998244353
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
    # return fac[n] * (finv[k] * finv[n - k]) % MOD


def main():
    com_init()
    n, m, k = map(int, input().split()) 

    ans = 0
    for i in range(0,k+1):
        ans += (m * com(n-1,i) * pow(m-1,n-i-1,MOD))
        ans %= MOD
    print(ans%MOD)



if __name__ == "__main__":
    main()

