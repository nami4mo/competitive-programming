n = int(input())

ans = []
for x in range(n-172,n):
    if x < 0: continue
    keta_sum = 0
    xs = str(x)
    for xsi in xs:
        keta_sum += int(xsi)
    if x + keta_sum == n:
        ans.append(x)

print(len(ans))
for a in ans:
    print(a)    