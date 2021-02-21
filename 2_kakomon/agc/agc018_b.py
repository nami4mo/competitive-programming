n,m=map(int, input().split())
al=[]
cnts=[0]*m
for _ in range(n):
    row=list(map(int, input().split()))
    row=[a-1 for a in row]
    al.append(row)
    cnts[row[0]]+=1

rems=[True]*m

max_i=-1
max_v=-1
for i in range(m):
    if cnts[i]>=max_v:
        max_i=i
        max_v=cnts[i]

curr_al=[]
for i in range(n):
    curr_al.append((al[i][0],0))

ans=max_v
for _ in range(m-1):
    rems[max_i]=False
    for j in range(n):
        if curr_al[j][0]!=max_i:continue
        while not rems[curr_al[j][0]]:
            next_i=curr_al[j][1]+1
            curr_al[j]=(al[j][next_i],next_i)
        cnts[curr_al[j][0]]+=1
    cnts[max_i]=0

    max_i=-1
    max_v=-1
    for i in range(m):
        if cnts[i]>=max_v:
            max_i=i
            max_v=cnts[i]
    ans=min(ans,max_v)

print(ans)