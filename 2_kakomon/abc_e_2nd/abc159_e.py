ans=10**10
h,w,k=map(int, input().split())
sl=[list(input()) for _ in range(h)]

from itertools import product
ite = list(product(range(2),repeat=h-1))
for pattern in ite:
    rows=[]
    c_rows=[0]*w
    cut=0
    for i, v in enumerate(pattern):
        row=sl[i]
        for j,s in enumerate(row):
            if s=='1':c_rows[j]+=1
        if v==1:
            rows.append(c_rows)
            c_rows=[0]*w
            cut+=1
    for j,s in enumerate(sl[-1]):
        if s=='1':c_rows[j]+=1
    rows.append(c_rows)

    hh=len(rows)
    cnts=[0]*hh
    for x in range(w):
        flag=False
        for y in range(hh):
            if rows[y][x]>k:
                cut+=10**10
                break
            if rows[y][x]+cnts[y]>k:
                flag=True
        if flag:
            cut+=1
            cnts=[0]*hh
            for y in range(hh):
                cnts[y]+=rows[y][x]
        else:
            for y in range(hh):
                cnts[y]+=rows[y][x]  

        if cut>=10**10:break
    # if cut==1:print(pattern)
    ans=min(ans,cut)
print(ans)