n=int(input())
s1=list(input())
s2=list(input())

alp_d = {chr(ord('A') + i): '.' for i in range(26)}
for _ in range(100):
    for i in range(n):
        a,b = s1[i], s2[i]
        if 'A' <= a <= 'Z' and alp_d[a] != '.':
            a = alp_d[a]
            s1[i] = a

        if 'A' <= b <= 'Z' and alp_d[b] != '.':
            b = alp_d[b]
            s2[i] = b

        if '0' <= a <= '9':
            if 'A' <= b <= 'Z':
                alp_d[b] = a
                s2[i] = a

        elif '0' <= b <= '9':
            if 'A' <= a <= 'Z':
                alp_d[a] = b
                s1[i] = b

ans = 1
top_c1 = ''
top_c2 = ''
used = set()
for i in range(n):
    if i == 0:
        if 'A' <= s1[i] <= 'Z':
            ans *= 9
            used.add(s1[i])
            used.add(s2[i])
        else:
            ans *= 1
    else:
        if 'A' <= s1[i] <= 'Z':
            if s1[i] in used or s2[i] in used:
                ans *= 1
            else:
                ans *= 10
            used.add(s1[i])
            used.add(s2[i])

print(ans)