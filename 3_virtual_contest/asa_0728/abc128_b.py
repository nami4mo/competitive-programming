n = int(input())

spl = {}
spl = []
for i in range(n):
    s,p = map(str, input().split())
    p = int(p)
    spl.append((s,p*(-1),i+1))
    # spl.setdefault(s,[])
    # spl[s].append((p,i+1))

spl.sort()
for s,p,i in spl:
    print(i)

# spl = sorted(spl.items(), key=lambda x:x[0])
# for s, pil in spl:
#     pil.sort()
#     for p,i in pil:
#         print(i)

 