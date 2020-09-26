from atcoder.string import suffix_array, lcp_array

s = input()
n = len(s)
sa = suffix_array(s)
# print(sa)
lcp = lcp_array(s,sa)
# print(lcp)

ans = n - sa[0]
for l, si in zip(lcp, sa[1:]):
    ans += (n-si-l)

print(ans)