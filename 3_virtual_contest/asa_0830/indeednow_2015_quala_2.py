n = int(input())
ansl = []
ss = 'indeednow'
ss = sorted(ss)
for _ in range(n):
    s = input()
    s = sorted(s)
    if s == ss:
        ansl.append('YES')
    else:
        ansl.append('NO')

for ans in ansl: print(ans)