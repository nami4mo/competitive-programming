from collections import Counter
s=input()
single=0
pair=0
c=Counter(s)
alps = 'abcdefghijklmnopqrstuvwxyz'
for a in alps:
    pair+=c[a]//2
    single+=c[a]%2

if single:
    v=pair//single
    print(v*2+1)
else:
    print(len(s))
