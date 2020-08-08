# 約数列挙
n = 16
for i in range(1, int(n**0.5)+1):
    if n%i == 0:
        print('yeah', i)
        if i*i != n:
            print('yeah', n//i)


# 60 -> {2:2, 3:1, 5:1}
# NOTE: n is large -> loop count is also large  ( O(√n) )
# GCDを求めるだけなら、素因数分解するより math.gcd の方が圧倒的に高速（ gcd: logN, 素因数分解: √n）
def factorization(n):
    if n == 1:
        return {}
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


# 60 -> [[2,2], [3,1], [5,1]]
def factorization_l(n):
    pf_cnt = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            pf_cnt.append([i,cnt])

    if temp != 1: pf_cnt.append([temp,1])
    if not pf_cnt: pf_cnt.append = [n,1]

    return pf_cnt


# modinv
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

MOD = 10**9 + 7
def pow_k(x, n):
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2
        x%=MOD
    return K * x

def pow_k(x, n):
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2
    return K * x
