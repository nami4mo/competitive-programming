'''
    [LCM]
'''
from math import gcd
def lcm(x,y): return (x * y) // gcd(x, y)



'''
    [約数列挙]
'''
n = 36
divs = []
for i in range(1, int(n**0.5)+1):
    if n%i == 0:
        divs.append(i)
        if i*i != n: divs.append(n//i)


'''
    [素数列挙] (N < 10^7)
'''
# https://python.ms/eratosthenes/#_2-%E9%AB%98%E9%80%9F%E7%89%88
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


'''
    [素因数分解]
'''
## (e.g) 60 -> {2:2, 3:1, 5:1}   1 -> {}
## NOTE: p_factorization... O(√N),  GCD... O(logN)
## GCDを求めるだけなら、素因数分解するより math.gcd の方が圧倒的に高速
def p_factorization(n):
    if n == 1: return {}
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
    return pf_cnt


## 60 -> [(2,2), (3,1), (5,1)]  (list of tuples)
def p_factorization_t(n):
    if n == 1: return []
    pf_cnt = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            pf_cnt.append((i,cnt))

    if temp != 1: pf_cnt.append((temp,1))
    return pf_cnt




'''
    [x^n]
'''
## NOTE: pow(x,n) か pow(x,n,MOD) で十分高速
MOD = 10**9 + 7
def pow_k(x, n):
    if n == 0: return 1
    K = 1
    while n > 1:
        if n%2 != 0: K *= x
        x *= x
        n //= 2
        x%=MOD
    return K * x


def pow_k(x, n):
    if n == 0: return 1
    K = 1
    while n > 1:
        if n%2 != 0: K *= x
        x *= x
        n //= 2
    return K * x
