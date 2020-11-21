from bisect import bisect_left, bisect_right

n = int(input())
wl = [int(input()) for _ in range(n)]
wl = wl[::-1]
l = [wl[0]]

for w in wl[1:]:
    ind = bisect_right(l, w) - 1
    if ind < 0:
        l = [w] + l[:]
    else:
        l[ind] = w
    # print(l)
print(len(l))