from itertools import product

n = int(input())
ansl = []
ite = product(range(3),repeat=n)
for it in ite:
    p = list(it)
    s = ''
    for i,v in enumerate(p):
        if v == 0: s += 'a'
        if v == 1: s += 'b'
        if v == 2: s += 'c'
    ansl.append(s)

for a in ansl:
    print(a)
