h,w,n=map(int, input().split())
rows=set()
cols=set()
abl=[]
for _ in range(n):
    a,b=map(int, input().split())
    a-=1
    b-=1
    rows.add(a)
    cols.add(b)
    abl.append((a,b))

rows=list(rows)
cols=list(cols)
rows.sort()
cols.sort()

rd={}
for i,v in enumerate(rows):
    rd[v]=i+1

cd={}
for i,v in enumerate(cols):
    cd[v]=i+1

for a,b in abl:
    aa=rd[a]
    bb=cd[b]
    print(aa,bb)