h,w=map(int, input().split())
al=[]
for _ in range(h):
    row=list(input())
    if '#' in row:
        al.append(row)

xl=set()
for x in range(w):
    for y in range(len(al)):
        if al[y][x]=='#':xl.add(x)

for row in al:
    rs=''
    for x in range(w):
        if x in xl:rs+=row[x]
    print(rs)