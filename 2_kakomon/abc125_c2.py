from fractions import gcd

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
    n = int(input())
    al = list(map(int, input().split()))

    # al_fac = [0]*n
    for i, a in enumerate(al):
        fac = factorization(a)
        # al_fac[i] = fac

    gcd_l = [1]*n
    gcd_r = [1]*n

    gcd_l[0] = al[0]
    gcd_r[-1] = al[-1]

    for i in range(1,n):
        next_l = al[i]
        gcd_l[i] = gcd(next_l, gcd_l[i-1])

        next_r = al[n-i-1]
        gcd_r[n-i-1] = gcd(next_r, gcd_r[n-i])


    ans = max(gcd_r[1], gcd_l[n-2])
    for i in range(1,n-1):
        curr_gcd = gcd(gcd_l[i-1], gcd_r[i+1])
        ans = max(ans, curr_gcd)

    print(ans)


if __name__ == "__main__":
    main()