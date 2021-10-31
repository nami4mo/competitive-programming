n,s = map(str, input().split())
n = int(n)

ans = 0
for i in range(n):
    a,g,c,t = 0,0,0,0
    for j in range(i,n):
        if s[j] == 'A': a += 1
        elif s[j] == 'G': g += 1
        elif s[j] == 'C': c += 1
        elif s[j] == 'T': t += 1
        if a == t and c == g: ans += 1

print(ans)

