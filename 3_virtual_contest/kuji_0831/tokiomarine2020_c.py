n,k = map(int, input().split())

al = list(map(int, input().split()))

for _ in range(min(100,k)):
    imos = [0]*(n+1)
    for i,a in enumerate(al):
        l = max(0,i-a)
        r = min(n,i+a+1)
        imos[l] += 1
        imos[r] -= 1
    new_al = []
    curr_val = 0
    for im in imos[:-1]:
        curr_val += im
        new_al.append(curr_val)
    al = new_al[:]

print(*al)