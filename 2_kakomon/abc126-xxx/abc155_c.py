n = int(input())
d = {}
for _ in range(n):
    s = input()
    d.setdefault(s,0)
    d[s] -= 1


t = []
for k,v in d.items():
    t.append((v,k))

t.sort()
num = t[0][0]
for v,s in t:
    if v == num:
        print(s)