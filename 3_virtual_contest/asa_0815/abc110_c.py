s = input()
t = input()

d = {}
for si,ti in zip(s,t):
    if not si in d:
        d[si] = ti
    else:
        if d[si] != ti:
            print('No')
            break
else:
    sset = set()
    for v in d.values():
        if v in sset:
            print('No')
            break
        sset.add(v)
    else:
        print('Yes')