n = int(input())
al = [0] + list(map(int, input().split())) + [0]
csum = 0
for a0,a1 in zip(al[:-1], al[1:]):
    v = abs(a1-a0)
    csum += v

ansl = []
for a0,a1,a2 in zip(al[:-2], al[1:-1], al[2:]):
    if a0 <= a1 <= a2 or a2 <= a1 <= a0:
        ansl.append(csum)
    elif a0 <= a1 and a1 >= a2:
        ansl.append(csum-(a1-max(a0,a2))*2)
    else:
        ansl.append(csum -(min(a2,a0)-a1)*2)

for a in ansl: print(a)