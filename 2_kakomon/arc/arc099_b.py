# n=int(input())
# for i in range(1,n):
#     v=sum([int(si) for si in str(i)])
#     print(i,i/v)

MAX=10**15
dic={}
for keta9 in range(0,13):
    bottom=pow(10,keta9)-1
    bottomup=pow(10,keta9)
    for not9num in range(0,10**4):
        val=not9num*bottomup+bottom
        if val==0:continue
        if val>MAX:continue
        bunbo=sum([int(si) for si in str(val)])
        dic[val]=val/bunbo

lis=[]
for k,v in dic.items():lis.append((k,v))
lis.sort()

snuke_nums=[]
cmin=lis[-1][1]
for k,v in lis[::-1]:
    if v<=cmin:snuke_nums.append(k)
    cmin=min(cmin,v)

snuke_nums=snuke_nums[::-1]

k=int(input())
for v in snuke_nums[:k]:print(v)