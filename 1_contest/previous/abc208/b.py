p=int(input())
vl=[1]
for i in range(1,10):
    vl.append(vl[-1]*(i+1))
# print(vl)
ans=0
for v in vl[::-1]:
    cnt=p//v
    p=p%v
    ans+=cnt
print(ans)