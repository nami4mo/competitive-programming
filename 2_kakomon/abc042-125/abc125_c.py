primes = []
def make_primes(n):
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            primes = prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


def factorization(n):
    pf_cnt = {}
    temp = n
    for p in primes:
        if temp%p == 0:
            cnt = 0
            while temp%p == 0:
                cnt += 1
                temp //= p
            pf_cnt[i] = cnt

    if temp != 1: pf_cnt[temp] = 1
    if not pf_cnt: pf_cnt[n] = 1

    return pf_cnt


def main():
    make_primes(10**9)
    n = int(input())
    al = list(map(int, input().split()))

    al_fac = [0]*n
    for i, a in enumerate(al):
        fac = factorization(a)
        al_fac[i] = fac

    gcd_l = [1]*n
    gcd_r = [1]*n

    gcd_l[0] = al_fac[0]
    gcd_r[-1] = al_fac[-1]

    for i in range(1,n):
        next_l = al_fac[i]
        next_l_gcd = {1:1}
        for prime,cnt in next_l.items():
            if prime in gcd_l[i-1]:
                next_l_gcd[prime] = min(cnt, gcd_l[i-1][prime])
        gcd_l[i] = next_l_gcd

        next_r = al_fac[n-i-1]
        next_r_gcd = {1:1}
        for prime,cnt in next_r.items():
            if prime in gcd_r[n-i]:
                next_r_gcd[prime] = min(cnt, gcd_r[n-i][prime])
        gcd_r[n-i-1] = next_r_gcd

    ans = 1
    for i in range(1,n-1):
        curr_gcd = 1
        for prime,cnt in gcd_l[i-1].items():
            if prime in gcd_r[i+1]:
                min_cnt = min(cnt, gcd_r[i+1][prime])
                curr_gcd *= prime**min_cnt
        ans = max(ans, curr_gcd)


    # i = 0
    curr_gcd = 1
    for prime,cnt in gcd_r[1].items():
        curr_gcd *= (prime**cnt)
    ans = max(ans, curr_gcd)

    # i = n-1
    curr_gcd = 1
    for prime,cnt in gcd_l[n-2].items():
        curr_gcd *= (prime**cnt)
    ans = max(ans, curr_gcd)

    # print(al_fac)
    # print(gcd_l)
    # print(gcd_r)
    print(ans)


if __name__ == "__main__":
    main()