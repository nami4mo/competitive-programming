n,m=map(int, input().split())
al=[]
for _ in range(2*n):
    row=input()
    al.append(row)

vs=[]
for i in range(2*n):
    vs.append((0,i))
    

for i in range(m):
    new_vs=[]
    for k in range(n):
        a=2*k
        b=2*k+1
        av=vs[a][0]
        bv=vs[b][0]
        a=vs[a][1]
        b=vs[b][1]
        if al[a][i]=='G' and al[b][i]=='C': av+=1
        if al[a][i]=='C' and al[b][i]=='P': av+=1
        if al[a][i]=='P' and al[b][i]=='G': av+=1

        if al[b][i]=='G' and al[a][i]=='C': bv+=1
        if al[b][i]=='C' and al[a][i]=='P': bv+=1
        if al[b][i]=='P' and al[a][i]=='G': bv+=1
        new_vs.append((av,a))
        new_vs.append((bv,b))
    new_vs.sort(key=lambda x:(-x[0],x[1]))
    vs=new_vs[:]
for i in range(2*n):
    print(vs[i][1]+1)