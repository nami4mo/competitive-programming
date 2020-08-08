# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c

import bisect

n, m = map(int, input().split()) 
al = []
for _ in range(n):
    al.append(int(input()))

two_sums = []
for i in range(n):
    for j in range(n):
        two_sums.append(al[i] + al[j])

two_sums = list(set(two_sums))
two_sums.sort()

res = 0
for ts in two_sums:
    max_two = m - ts
    insert_index = bisect.bisect_left(two_sums, max_two)
    if insert_index == 0:
        if ts == m:
            res = m
            break
    else:
        res = max(res, ts+two_sums[insert_index-1])

print(res)