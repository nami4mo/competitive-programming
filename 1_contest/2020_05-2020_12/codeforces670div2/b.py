ansl = []
for _ in range(int(input())):
    n = int(input())
    al = list(map(int, input().split()))
    al.sort()
    alm = []
    alp = []
    zero = 0
    for a in al:
        if a > 0: alp.append(a)
        elif a < 0: alm.append(-a)
        else: zero += 1

    if alp: alp.sort(reverse=True)
    ans = (-1)*(10**18)
    if len(alm) >= 4 and len(alp) >= 1:
        v = alm[0]*alm[1]*alm[2]*alm[3] *alp[0]
        ans = max(ans,v)
    if len(alm) >= 2 and len(alp) >= 3:
        v = alm[0]*alm[1] *alp[0]*alp[1]*alp[2]
        ans = max(ans,v)
    if len(alp) >= 5:
        v = alp[0]*alp[1]*alp[2]*alp[3]*alp[4]
        ans = max(ans,v)

    if zero > 0: ans = max(ans,0)

    if len(alm) >= 5:
        v = alm[-1]*alm[-2]*alm[-3]*alm[-4]*alm[-5]
        ans = max(ans,-v)
    if len(alm) >= 3 and len(alp) >= 2:
        v = alm[-1]*alm[-2]*alm[-3] *alp[-1]*alp[-2]
        ans = max(ans,-v)
    if len(alm) >= 1 and len(alp) >= 4:
        v = alm[-1] *alp[-1]*alp[-2]*alp[-3]*alp[-4]
        ans = max(ans,-v)

    ansl.append(ans)

for a in ansl: print(a)

