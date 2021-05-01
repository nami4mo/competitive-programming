import sys
sys.setrecursionlimit(10**7)

def rec(cl, csum, cnt, lim, res):
    if cnt==10:
        res.append(cl)
        return

    rem=lim-csum
    for i in range(rem+1):
        rec(cl+[i], csum+i, cnt+1, lim, res)

n,b=map(int, input().split())
res=[]
rec([],0,0,11,res)
# print(res)
ans=0
for cl in res:
    p=1
    for i,c in enumerate(cl):
        if i==0:continue
        p*=pow(i,c)
    want=b+p
    if want>n:continue
    cnts=[0]*10
    for si in str(want):
        cnts[int(si)]+=1

    for i in range(10):
        if i==0 and cnts[i]>0:break
        if cnts[i]!=cl[i]:break
    else:
        ans+=1
if '0' in str(b) and n>=b: ans+=1
print(ans)