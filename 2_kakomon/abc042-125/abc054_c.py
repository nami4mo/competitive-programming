from itertools import permutations

n,m = map(int, input().split())
gl = [ [False]*(n+1) for _ in range(n+1) ]
for _ in range(m):
    a,b = map(int, input().split())
    gl[a][b] = True
    gl[b][a] = True


ll = list(range(2,n+1))  # list of elements
perml = list(permutations(ll, n-1))
ans = 0

for perm in perml:
    curr = 1
    for v in perm:
        if gl[curr][v]:
            curr = v
        else:
            break
    else:
        ans += 1

print(ans)