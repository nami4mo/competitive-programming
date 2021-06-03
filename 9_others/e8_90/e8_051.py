n,k,p=map(int, input().split())
al=list(map(int, input().split()))
n2=n//2
n1=n-n2

al1=al[:n1]
al2=al[n1:]

if n1!=n2:
    n2+=1
    al2.append(p+1)

sum1=[[] for _ in range(n1+1)]
sum2=[[] for _ in range(n2+1)]
sum1[0].append(0)
sum2[0].append(0)

from itertools import product
ite = list(product(range(2),repeat=n1))
for pattern in ite:
    val1=0
    cnt1=0
    val2=0
    cnt2=0
    for i, v in enumerate(pattern):
        if v==1: 
            val1+=al1[i]
            cnt1+=1
            val2+=al2[i]
            cnt2+=1
    if cnt1>0:sum1[cnt1].append(val1)
    if cnt2>0:sum2[cnt2].append(val2)


for i in range(n1+1):
    sum1[i].sort()
    sum2[i].sort()

from bisect import bisect_left, bisect_right

ans=0
for i in range(min(k+1,n1+1)):
    if not 0<=k-i<=n2: continue
    for a in sum1[i]:
        rem=p-a
        cnt = bisect_right(sum2[k-i], rem)
        ans+=cnt
print(ans)