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
    for a in al:
        fac = factorization(a)
        for f in fac:
            lcm_dic[f[0]] = max(f[1], lcm_dic[f[0]])


    lcm = 1
    for prime, cnt in lcm_dic.items():
        lcm *= pow_k1(prime,cnt)

    
    ans = 0
    for a in al:
        ans += (lcm//a)%MOD
        # if ans >= MOD: ans%=MOD
    ans%=MOD

    print(ans)


if __name__ == "__main__":
    main()