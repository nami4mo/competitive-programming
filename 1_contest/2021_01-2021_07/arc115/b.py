n=int(input())
cl=[]
for _ in range(n):
    row=list(map(int, input().split()))
    cl.append(row)

ad=[]
amin=0
v=0
for i in range(n-1):
    d=cl[i+1][0]-cl[i][0]
    ad.append(d)
    v+=d
    amin=max(-v,amin)
    # print(v)


for j in range(n):
    for i in range(n-1):
        d=cl[i+1][j]-cl[i][j]
        if ad[i]!=d:
            print('No')
            exit()

bd=[]
bmin=0
v=0
for j in range(n-1):
    d=cl[0][j+1]-cl[0][j]
    bd.append(d)
    v+=d
    bmin=max(-v,bmin)

for i in range(n):
    for j in range(n-1):
        d=cl[i][j+1]-cl[i][j]
        if bd[j]!=d:
            print('No')
            exit()

if amin+bmin>cl[0][0]:
    print('No')
    exit()

rem=cl[0][0]-amin-bmin
amin+=rem

print('Yes')
al=[amin]
bl=[bmin]

for d in ad:
    al.append(al[-1]+d)
for d in bd:
    bl.append(bl[-1]+d)
print(*al)
print(*bl)