from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
col_maxs = []
for _ in range(n):
    a = int(input()) * (-1)
    if not col_maxs:
        col_maxs.append(a)
        continue

    curr_max = col_maxs[-1]
    if a >= curr_max:
        col_maxs.append(a)
    else:
        # aより大きい最小要素のindex/value
        ind = bisect_right(col_maxs, a)
        col_maxs[ind] = a

print(len(col_maxs))