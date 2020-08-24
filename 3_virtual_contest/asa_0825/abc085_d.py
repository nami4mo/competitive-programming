n,h = map(int, input().split())
al = []
bl = []
for _ in range(n):
    a,b = map(int, input().split())
    al.append(a)
    bl.append(b)

al.sort(reverse=True)
bl.sort(reverse=True)

amax = al[0]
ans = 0
rem = h
for b in bl:
    if b >= amax:
        rem -= b
        ans += 1
    else:
        break
    if rem <= 0:
        print(ans)
        exit()

cnt = (rem-1)//amax + 1
ans += cnt
print(ans)