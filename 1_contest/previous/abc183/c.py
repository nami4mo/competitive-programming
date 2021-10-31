from itertools import permutations

n,k = map(int, input().split())
tll = [list(map(int, input().split())) for _ in range(n)]

ll = list(range(1,n))  # list of elements
perml = list(permutations(ll, n-1))

# print(perml)

ans = 0
for perm in perml:
    ro = [0] + list(perm) + [0]
    dist = 0
    for i in range(len(ro)-1):
        d = tll[ro[i]][ro[i+1]]
        dist += d
    if dist == k:
        ans += 1

print(ans)