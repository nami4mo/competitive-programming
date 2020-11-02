from bisect import bisect_left, bisect_right

n,m = map(int, input().split())
hl = list(map(int, input().split()))
wl = list(map(int, input().split()))
hl.sort()
wl.sort()

csum = [0]
csumr = [0]

c = 0
for i in range(n//2):
    v = hl[i*2+1] - hl[i*2]
    c+=v
    csum.append(c)

c = 0
for i in range(n//2):
    v = hl[n-1-i*2] - hl[n-2-i*2]
    c+=v
    csumr.append(c)

# print(csum)
# print(csumr)

# ;ast n+1
ans = 10**20
for i in range(n):
    hv = hl[i]

    ind1 = bisect_right(wl, hv) - 1
    ind1 = ind1 if 0 <= ind1 < m else None        # -> 7
    val1 = wl[ind1] if ind1 is not None else 10**18  # -> 6s
    ind3 = bisect_left(wl, hv)
    ind3 = ind3 if 0 <= ind3 < m else None        # -> 6
    val3 = wl[ind3] if ind3 is not None else 10**18 # -> 6

    diff = min( abs(val1-hv), abs(val3-hv))

    if i%2 == 0:
        # if i == 0:
        #     front_sum = 0
        # else:
        front_sum = csum[i//2]
        back_sum = csumr[n//2-i//2]
        cand = diff + front_sum + back_sum
        ans = min(ans,cand)
    else:
        front_sum = csum[i//2]
        back_sum = csumr[n//2-i//2-1]
        three = hl[i+1]-hl[i-1]
        cand = diff + front_sum + back_sum + three
        ans = min(ans,cand)

print(ans)

