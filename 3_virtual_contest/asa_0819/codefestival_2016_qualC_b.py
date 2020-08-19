k,t = map(int, input().split())
al = list(map(int, input().split()))

prev = -1
ans = 0
for i in range(k):
    max_v = max(al)
    max_ind = al.index(max_v)
    max_v = 0
    max_i = -1
    for j, v in enumerate(al):
        if max_v < v and j != prev:
            max_v = v
            max_i = j
    if max_i != -1:
        al[max_i] -= 1
        prev = max_i
    else:
        ans += 1

print(ans)