n, m, q = map(int, input().split()) 
g = [ [] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split()) 
    g[a].append(b)
    g[b].append(a)

c_list = [0]
c_list.extend(list(map(int, input().split())) )

sl = []
for _ in range(q):
    sl.append(list(map(str, input().split())) )

for s in sl:
    x = int(s[1])
    print(c_list[x])
    if s[0] == '1':
        for neib in g[x]:
            c_list[neib] = c_list[x]
    else:
        c_list[x] = int(s[2])

