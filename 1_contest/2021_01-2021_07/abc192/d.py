x=input()
m=int(input())
if len(x)==1:
    if int(x)<=m:
        print(1)
    else:
        print(0)
    exit()



x=[int(v) for v in x[::-1]]

# print(x)
maxd=max(x)
# print(maxd)
ok, ng = 0, 10**19+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True
    val=0
    # print(mid,'---')
    for i in range(len(x)):
        val+=pow(mid,i)*x[i]
        # print(val)
        if val>m:
            res=False
            break
    if res: ok = mid
    else: ng = mid
ans=ok-maxd
if ans<=0:ans=0
print(ans)