from itertools import permutations
from math import sqrt

n = int(input())
xyl = []
for _ in range(n):
    x,y = map(int, input().split())
    xyl.append((x,y))

ll = list(range(0,n))
perml = list(permutations(ll, n))

val = 0
for perm in perml:
    prev_x = 0
    prev_y = 0
    for i,p in enumerate(perm):
        x,y = xyl[p]
        if i == 0:
            prev_x = x
            prev_y = y
        else:
            val += sqrt( (prev_x-x)**2 + (prev_y-y)**2 )
            prev_x = x
            prev_y = y
    
ans = val/len(perml)
print(ans)