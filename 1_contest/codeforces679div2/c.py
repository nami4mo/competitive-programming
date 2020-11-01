import sys
input = sys.stdin.readline

al = list(map(int, input().split()))
n = int(input())
bl = list(map(int, input().split()))
al.sort(reverse=True)
bl.sort()

mms = []
fs = []
for a in al:
    f = bl[0]-a
    if f <= 0: continue
    mms.append((f,f))

for b in bl[1:]:
    fcands = []
    new_mms_d = {}
    for a in al:
        f = b-a
        if f <= 0: continue
        fcands.append(f)
    for mm in mms:
        l = -1
        r = 10**10
        for f in fcands:
            if mm[0] <= f <= mm[1]:
                # new_mms.append(mm)
                if mm[0] in new_mms_d and new_mms_d[mm[0]] <= mm[1]:
                    pass
                else:
                    new_mms_d[mm[0]] = mm[1]
                break
            if f < mm[0]:
                l = max(l,f)
            elif mm[1] < f:
                r = min(r,f)
        else:
            if l != -1:
                if l in new_mms_d and new_mms_d[l] <= mm[1]:
                    pass
                else:
                    new_mms_d[l] = mm[1]
            if r != 10**10:
                if mm[0] in new_mms_d and new_mms_d[mm[0]] <= r:
                    pass
                else:
                    new_mms_d[mm[0]] = r
    mms = []
    md = {}
    for k, v in new_mms_d.items():
        if v in md and md[v] > k: continue
        md[v] = k
    for k,v in md.items():
        mms.append((v,k))
        # mms.append((k,v))
    # for k, v in new_mms_d.items():
    #     mms.append((k,v))
    # mms
    # new_mms.sort()
    # for mms 

# print(mms)
ans = 10**10
for mm in mms:
    ans = min(mm[1]-mm[0],ans)
print(ans)