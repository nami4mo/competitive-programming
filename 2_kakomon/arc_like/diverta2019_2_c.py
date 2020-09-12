import bisect

n = map(int, input().split())
A = list(map(int, input().split()))

pl= []
ml = []
for a in A:
    if a >= 0: pl.append(a)
    else: ml.append(a)

pl.sort()
ml.sort()

ans = 0
ans_l = []


if pl and ml:
    ans = ml[0]
    for p in pl[1:]:
        ans_l.append((ans,p))
        ans -= p
    ans_l.append((pl[0], ans))
    ans = pl[0] - ans
    for m in ml[1:]:
        ans_l.append((ans,m))
        ans -= m

elif not pl: # only ml
    ans = ml[-1]
    for m in ml[:-1]:
        ans_l.append((ans,m))
        ans -= m

else: # only pl
    ans = pl[0]
    for p in pl[1:-1]:
        ans_l.append((ans,p))
        ans -= p
    ans_l.append((pl[-1], ans))
    ans = pl[-1] - ans

print(ans)
for row in ans_l:
    print(row[0], row[1])