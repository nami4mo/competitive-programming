ansl=[]
for dbg in range(int(input())):
    n,c=map(int, input().split())
    # n=10
    # c=dbg
    need=c-(n-1)
    if need<0:
        ansl.append([])
        continue
    al=list(range(1,n+1))
    for i in range(n-2,-1,-1):
        if need==0:break
        d=min(n-1-i, need)
        # print(d)
        j=i+d
        new_al=[]
        # print(i,j)
        for k in range(i):
            new_al.append(al[k])
        for k in range(i,j+1):
            ind=i+j-k
            new_al.append(al[ind])
        for k in range(j+1,n):
            new_al.append(al[k])
        al=new_al[:] 
        need-=d
        # print(al)
    if need==0:
        ansl.append(al)
    else:
        ansl.append([])

for i,a in enumerate(ansl):
    ans=''
    for ai in a:
        ans+=str(ai)
        ans+=' '
    ans.rstrip()
    if a:
        print(f'Case #{i+1}: {ans}')
    else:
        print(f'Case #{i+1}: IMPOSSIBLE')