from itertools import permutations
n, k = 3, 3
ll = list(range(0,n))  # list of elements
perml = list(permutations(ll, k))

al = list(map(int, input().split()))
bl = list(map(int, input().split()))

ans = 0
for p in perml:
    val = 1
    for i,v in enumerate(p):
        val *= al[v]//bl[i] 
    ans = max(val,ans)

print(ans)