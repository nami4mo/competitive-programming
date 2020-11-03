import sys
input = sys.stdin.readline

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

# print(len(primes(400)))

for _ in range(int(input())):
    n = int(input())
    ps = primes(4*n)
    ansl = []
    f2 = 4
    for i in range(10):
        if f2*2 > 4*n:
            break
        else:
            f2*=2
    o2 = f2//2
    ansl.append(f2)
    rem = 4*n//o2
    cnt = 0
    for p in ps[1:]:
        # print(p,'--')
        f = p
        # powc = 1
        for i in range(10):
            if f*p > 4*n:
                break
            else:
                f*=p
                # powc+=1
        print(f)
        if f*2 > 4*n:
            continue
        co2 = 2
        end = False
        while True:
            ansl.append(co2*f)
            cnt += 1
            if cnt == n:
                print(*ansl)
                end = True
                break
            f//=p
            co2 *= 2
            if f == 1 or co2 == f2:
                break 
        if end: break
        