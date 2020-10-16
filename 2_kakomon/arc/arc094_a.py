al = list(map(int, input().split()))
al.sort()

if al[0] == al[2]:
    print(0)
    exit()

ans = 0
d = al[1]-al[0]
if d%2 == 0:
    ans += d//2
    ans += al[2]-al[1]
else:
    ans += d//2
    ans += al[2]-al[1]
    ans += 2

print(ans)
