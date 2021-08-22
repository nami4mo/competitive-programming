n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
bl=bl[::-1]

same_inds=[]
same_num=-1
for i in range(n):
    if al[i]==bl[i]: 
        same_inds.append(i)
        same_num=al[i]

if al.count(same_num)+bl.count(same_num) > n:
    print('No')
    exit()

swaped_inds=[]
for i in range(n):
    if bl[i]!=same_num and al[i]!=same_num:
        swaped_inds.append(i)
    if len(swaped_inds) == len(same_inds):
        break

for i1,i2 in zip(same_inds,swaped_inds):
    bl[i1],bl[i2] = bl[i2],bl[i1]

print('Yes')
print(*bl)