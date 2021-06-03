def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return is_prime

ans=0
ps=primes(1000)
al=[list(map(int, input().split())) for _ in range(20)]
for row in al:
    for a in row:
        if ps[a]:ans+=1
print(ans)