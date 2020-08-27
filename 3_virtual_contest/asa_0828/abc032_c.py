n,k = map(int, input().split())
sl = []
for _ in range(n):
    sl.append(int(input()))

if 0 in sl:
    print(n)
    exit()

val = sl[0]
l = 0
r = 1
if val > k:
    for i in range(n):
        if sl[i] <= k:
            val = sl[i]
            l = i
            r = i+1
            break
    else:
        print(0)
        exit()

ans = 0
while True:
    # print(l,r,val)
    if r >= n:
        break
    next_s = sl[r]
    if next_s * val <= k:
        val *= next_s
        r += 1
        ans = max(ans,r-l)
    else:
        val//=sl[l]
        l += 1

print(ans)