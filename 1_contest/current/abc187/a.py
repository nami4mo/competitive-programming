a,b=map(str, input().split())
aa=0
bb=0
for ai in a:
    aa+=int(ai)
for bi in b:
    bb+=int(bi)
print(max(aa,bb))