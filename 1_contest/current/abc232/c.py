from itertools import permutations
n, m = map(int, input().split())

abl = [[] for _ in range(n)]
cdl = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a
    abl[a].append(b)
    abl[b].append(a)

for i in range(n):
    abl[i].sort()

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a
    cdl[a].append(b)
    cdl[b].append(a)

# print(abl)
# print(cdl)

ll = list(range(n))  # list of elements
perml = list(permutations(ll, n))

for perm in perml:
    perm = list(perm)
    efl = [[] for _ in range(n)]
    for i in range(n):
        for v in cdl[i]:
            ii = perm[i]
            vv = perm[v]
            efl[ii].append(vv)
            # efl[vv].append(ii)
    for i in range(n):
        efl[i].sort()
    if abl == efl:
        print('Yes')
        exit()
    # print(abl)
    # print(efl)
    # print('---')
print('No')
