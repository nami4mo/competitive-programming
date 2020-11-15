n,w = map(int, input().split())

T_MAX = 2*(10**5)+1
imos = [0]*(T_MAX)

for _ in range(n):
    s,t,p = map(int, input().split())
    imos[s] += p
    imos[t] -= p

cnts = [0]*(T_MAX)
curr = 0
for i in range(T_MAX):
    curr += imos[i]
    cnts[i] = curr

if max(cnts) <= w:
    print('Yes')

else:
    print('No')