MAX = 10**6+1
n = int(input())
imos = [0]*(MAX+1)

for _ in range(n):
    a,b = map(int, input().split())
    imos[a] += 1
    imos[b+1] -= 1

cnts = [0]*(MAX+1)
cnt = 0
for i, imo in enumerate(imos):
    cnt += imo
    cnts[i] = cnt

print(max(cnts))