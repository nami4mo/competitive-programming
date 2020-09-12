import sys
from collections import deque, Counter, defaultdict

input = sys.stdin.readline
MOD = (10**9+7)

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr


def pow_k1(x, n):
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2
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
        x%=MOD
    return K * x


def main():
    n = int(input())
    al = list(map(int, input().split())) 
    lcm_dic = defaultdict(int)
    # lcm_dic = {}
    # al_facs = []
    for a in al:
        fac = factorization(a)
        # a_fac_dic = {}
        for f in fac:
            # lcm_dic.setdefault(f[0],0)
            lcm_dic[f[0]] = max(f[1], lcm_dic[f[0]])
            # a_fac_dic[f[0]] = f[1]
        # al_facs.append(a_fac_dic)


    lcm = 1
    for prime, cnt in lcm_dic.items():
        lcm *= pow_k1(prime,cnt)

    
    ans = 0
    for a in al:
        ans += (lcm//a)%MOD
        # if ans >= MOD: ans%=MOD
    ans%=MOD


    # ans = 0
    # for al_f in al_facs:
    #     curr_val = 1
    #     for prime, cnt in lcm_dic.items():
    #         if prime in al_f:
    #             curr_val *= pow_k(prime,(cnt-al_f[prime]))
    #             curr_val%=MOD
    #         else:
    #             curr_val *= pow_k(prime,cnt)
    #             curr_val%=MOD
    #     ans += curr_val
    #     ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()