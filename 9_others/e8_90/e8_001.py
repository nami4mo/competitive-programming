n,l=map(int, input().split())
k=int(input())
al=[0]+list(map(int, input().split()))+[l]
ps=[]
for i in range(len(al)-1):
    d=al[i+1]-al[i]
    ps.append(d)
ok, ng = 0, 10**9+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True
    # ...
    cnt=0
    c=0
    for p in ps:
        c+=p
        if c>=mid:
            c=0
            cnt+=1
    else:
        res=(cnt>=k+1)
    if res: ok = mid
    else: ng = mid
print(ok)