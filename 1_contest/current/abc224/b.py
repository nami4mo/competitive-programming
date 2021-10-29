h,w=map(int, input().split())
al=[]
for _ in range(h):
    row=list(map(int, input().split()))
    al.append(row)

for i1 in range(h):
    for i2 in range(i1+1,h):
        for j1 in range(w):
            for j2 in range(j1+1,w):
                if al[i1][j1]+al[i2][j2]>al[i2][j1]+al[i1][j2]:
                    print('No')
                    exit()
print('Yes')