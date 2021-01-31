
n=int(input())
sel=[]
for _ in range(n):
    row=input()
    s,e=row.split('-')
    s,e=int(s),int(e)
    s-=s%5
    if e%5!=0:
        e+=(5-e%5)
    if e%100==60:
        e+=40
    sel.append((s,e))

sel.sort()
# print(sel)

ansl=[]
cs,ce=sel[0]
for s,e in sel:
    if s<=ce:
        ce=max(e,ce)
    else:
        ansl.append(f'{cs:04}-{ce:04}')
        cs=s
        ce=e

ansl.append(f'{cs:04}-{ce:04}')
for a in ansl:print(a)