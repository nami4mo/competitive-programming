h,w,m = map(int, input().split())

hl = [0]*(h+1)
wl = [0]*(w+1)

hw_set = set()
for _ in range(m):
    ch,cw = map(int, input().split())
    hl[ch] += 1
    wl[cw] += 1
    hw_set.add((ch,cw))

hl_vi = []
for i, v in enumerate(hl):
    hl_vi.append((v,i))
hl_vi.sort(reverse=True)

wl_vi = []
for i, v in enumerate(wl):
    wl_vi.append((v,i))
wl_vi.sort(reverse=True)

max_h = hl_vi[0][0]
max_hil = []
for v,i in hl_vi:
    if v == max_h:
        max_hil.append(i)

max_w = wl_vi[0][0]
max_wil = []
for v,i in wl_vi:
    if v == max_w:
        max_wil.append(i)


for hi in max_hil:
    for wi in max_wil:
        if not (hi,wi) in hw_set:
            ans = max_h + max_w
            print(ans)
            exit()
            
ans = max_h + max_w
print(ans-1)

# print(max_hil)
# print(max_wil)

# print(hl_vi)
# print(wl_vi)
# ans = hl_vi[0][0] + wl_vi[0][0]
# if (hl_vi[0][1], wl_vi[0][1]) in hw_set:
#     ans-=1

# print(ans)

