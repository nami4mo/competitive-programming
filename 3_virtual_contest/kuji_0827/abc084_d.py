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

sums = [0,0,0]
curr_sum = 0
ps = primes(10**3)
pset = set(ps)
for i in range(3,10**5+1):
    for p in ps:
        if i%p == 0 and i not in pset:
            break
        if ((i+1)//2)%p == 0 and ((i+1)//2) not in pset:
            break
    else:
        curr_sum += 1
        # print(i)
    sums.append(curr_sum)
    

q = int(input())
ansl = []
for _ in range(q):
    l,r = map(int, input().split())
    ans = sums[r] - sums[l-1]
    ansl.append(ans)

for a in ansl: print(a)

# print(sums[:54])
