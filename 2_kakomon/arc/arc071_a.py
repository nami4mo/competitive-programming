n = int(input())
alps = 'abcdefghijklmnopqrstuvwxyz'
alp_d = {}
for a in alps:
    alp_d[a] = 1000

for _ in range(n):
    s = input()
    for a in alps:
        alp_d[a] = min(alp_d[a], s.count(a))

ans = ''
for a in alp_d:
    if alp_d[a] > 0:
        ans += a*alp_d[a]
print(ans)