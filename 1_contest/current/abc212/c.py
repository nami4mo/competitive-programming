n,m=map(int, input().split())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))

al.sort()
bl.append(-10**18)
bl.append(10**18)
bl.sort()

ans=10**18

from bisect import bisect_left, bisect_right

for a in al:
    ind1 = bisect_right(bl, a) - 1
    ind1 = ind1 if 0 <= ind1 < m+2 else None        # -> 7
    val1 = bl[ind1] if ind1 is not None else None  # -> 6

    ind3 = bisect_left(bl, a)
    ind3 = ind3 if 0 <= ind3 < m+2 else None        # -> 6
    val3 = bl[ind3] if ind3 is not None else None # -> 6

    ans=min(ans, abs(a-val1))
    ans=min(ans, abs(a-val3))
print(ans)