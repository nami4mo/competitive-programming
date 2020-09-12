from math import gcd

def p_factorization_osa_k(vl):
    vmax = max(vl)
    min_primes = list(range(vmax+1))  # initialize all values by its own value
    for i in range(2, int(vmax**0.5) + 1):
        if min_primes[i] != i: continue  # if not prime
        for j in range(i,vmax+1,i): 
            min_primes[j] = min(min_primes[j], i) # -> if min_primes[j] == j: min_primes[j] = i
    results = []
    for v in vl:
        p_cnt = {}
        curr_v = v
        while curr_v > 1:
            min_p = min_primes[curr_v]
            p_cnt.setdefault(min_p,0)
            p_cnt[min_p] += 1
            curr_v //= min_p
        results.append(p_cnt)
    return results


n = int(input())
al = list(map(int, input().split()))
afl = p_factorization_osa_k(al)

pset = set()
no_pairwise = False
for af in afl:
    for p in af.keys():
        if p in pset:
            no_pairwise = True
            break
        pset.add(p)
    if no_pairwise:
        break
else:
    print('pairwise coprime')
    exit()


c_gcd = al[0]
for a in al[1:]:
    c_gcd = gcd(c_gcd,a)

if c_gcd == 1: print('setwise coprime')
else: print('not coprime')