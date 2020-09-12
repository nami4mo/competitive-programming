n = int(input())
md = {'M':0, 'A':0 , 'R':0, 'C':0, 'H':0}
for _ in range(n):
    s = input()
    if s[0] in md:
        md[s[0]] += 1

vs = []
for v in md.values():
    vs.append(v)

ans = 0
for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            ans += vs[i]*vs[j]*vs[k]

print(ans)