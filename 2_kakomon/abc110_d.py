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


# 60 -> {2:2, 3:1, 5:1}
def factorization(n):
    pf_cnt = {}
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            pf_cnt[i] = cnt

    if temp != 1: pf_cnt[temp] = 1
    if not pf_cnt: pf_cnt[n] = 1

    return pf_cnt


def main():
    com_init()
    n, m = map(int, input().split())
    if m == 1:
        print(1)
        return
        
    fac = factorization(m)
    prime_combs = []
    for prime, cnt in fac.items():
        prime_combs.append(com(n-1+cnt, cnt))

    ans = 1
    for c in prime_combs:
        ans*=c
        ans%=MOD

    print(ans)

if __name__ == "__main__":
    main()