from collections import deque
from atcoder.string import z_algorithm

n = int(input())
s = input()

ans = 0
for i in range(n):
    zs = z_algorithm(s[i:])
    for j in range(i+1,n):
        ind = j-i
        dist = j-i
        v = min(dist,zs[ind])
        ans = max(ans,v)

print(ans)