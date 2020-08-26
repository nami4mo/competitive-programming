n,h = map(int, input().split())
al = []
bl = []
for _ in range(n):
    a,b = map(int, input().split())
    al.append(a)
    bl.append(b)

al.sort(reverse=True)
bl.sort(reverse=True)

rem = h
ans = 0
for b in bl:
    if b >= al[0]:
        ans += 1
        rem -= b
    if rem <= 0:
        print(ans)
        exit()

cnt = (rem-1)//al[0]+1
print(ans+cnt)