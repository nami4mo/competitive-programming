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

ps=primes(50)
pn=len(ps)
n=int(input())
xl=list(map(int, input().split()))

from math import gcd
ans=10**20
from itertools import product
ite = list(product(range(2),repeat=pn))
for pattern in ite:
    val=1
    for i, v in enumerate(pattern):
        if v==1:val*=ps[i]

    for x in xl:
        if gcd(x,val)==1:break
    else:
        ans=min(ans,val)
print(ans)


# print(xl)

# st=list(xl)
# ans=1
# for p in ps:
#     xll=list(st)
#     res=False
#     print(xll)
#     for x in xll:
#         if x%p==0:
#             res=True
#             st.remove(x)
#     if res:ans*=p
#     print(st,p,ans)
# print(ans)