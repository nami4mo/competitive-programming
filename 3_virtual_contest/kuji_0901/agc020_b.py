from math import ceil, floor

k = int(input())
al = list(map(int, input().split()))
al = al[::-1]

l,r = -1,-1
if al[0] != 2:
    print(-1)
    exit()

l = 2
r = 3
for a in al[1:]:
    min_l = ceil(l/a)*a
    max_r = floor(r/a)*a
    if min_l > r:
        print(-1)
        exit()
    if max_r < l:
        print(-1)
        exit()
    l = min_l
    r = max_r + (a-1)

print(l,r)