n = int(input())
cl = []
for _ in range(n):
    c = int(input())
    cl.append(c)

cl = cl+cl
if 0 not in cl or 1 not in cl:
    print(-1)
    exit()


max_first = True
cnt = 0
max_c = 0
prev = cl[0]
for c in cl:
    if c == prev:
        cnt += 1
    else:
        max_c = max(cnt,max_c)
        cnt = 1
    prev = c

ans = (max_c+1)//2
print(ans)
    