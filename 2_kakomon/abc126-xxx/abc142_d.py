from math import gcd

def factorization(n):
    pf_cnt = {}
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            if i != 1: pf_cnt[i] = cnt

    if temp != 1: pf_cnt[temp] = 1
    if not pf_cnt and n != 1: pf_cnt[n] = 1

    return pf_cnt

a,b = map(int, input().split())
ab_gcd = gcd(a,b)
fac = factorization(ab_gcd)
print(len(fac)+1)