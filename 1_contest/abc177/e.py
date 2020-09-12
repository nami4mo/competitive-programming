from math import gcd

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


def main():
    n = int(input())
    al = list(map(int, input().split()))
    als = [0]*(10**6+1)
    for a in al:
        als[a] += 1

    ps = primes(10**6)
    for p in ps:
        cnt = 0
        for i in range(p,10**6+1,p):
            cnt += als[i]
        if cnt >= 2:
            break
    else:
        print('pairwise coprime')
        exit() 

    c_gcd = al[0]
    for a in al[1:]:
        c_gcd = gcd(c_gcd,a)
    
    if c_gcd == 1:
        print('setwise coprime')
    else:
        print('not coprime')

if __name__ == "__main__":
    main()