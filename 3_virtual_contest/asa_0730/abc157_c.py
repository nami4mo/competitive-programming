n,m = map(int, input().split())
cond = []
for _ in range(m):
    s,c = map(int, input().split())
    cond.append((s,c))


for i in range(0,1000):
    num_s = str(i)
    if len(num_s) != n:
        continue

    for s,c in cond:
        if len(num_s) < s or num_s[s-1] != str(c):
            break
    else:
        print(i)
        exit()

else:
    print(-1)
    