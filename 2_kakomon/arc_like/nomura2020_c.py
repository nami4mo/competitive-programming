def fail():
    print(-1)
    exit()

n=int(input())
al=list(map(int, input().split()))
maxl=[]
csum=0
for i in range(n,0,-1):
    csum+=al[i]
    maxl.append(csum)
maxl=maxl[::-1]
# print(maxl)

if n==0:
    if al[0]==1:print(1)
    else:print(-1)
    exit()

if al[0]!=0:fail()

curr_not_leaf=1
ans=1
for i in range(n):
    next_max=curr_not_leaf*2
    next_leaf=al[i+1]
    next_cnt=min(next_max,maxl[i])
    ans+=next_cnt
    if next_cnt<next_leaf:fail()
    curr_not_leaf = next_cnt-next_leaf

print(ans)