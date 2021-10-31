ansl=[]
for _ in range(int(input())):
    n=int(input())
    al=list(map(int, input().split()))
    ans=0
    for i in range(n-1):
        mv,mj=10000,-1
        for j in range(i,n):
            if al[j]<mv:
                mv=al[j]
                mj=j
        new_al=[]
        for k in range(i):
            new_al.append(al[k])
        for k in range(i,mj+1):
            ind=i+mj-k
            new_al.append(al[ind])
        for k in range(mj+1,n):
            new_al.append(al[k])
        al=new_al[:]
        ans+=(mj-i+1)
    ansl.append(ans)

for i,a in enumerate(ansl):
    print(f'Case #{i+1}: {a}')
