from math import log,ceil

eps=10**(-10)
al=[]
for _ in range(int(input())):
    a,b=map(int, input().split())
    if a==1:
        if b==1:al.append(2)
        else:al.append(1)
        continue
    if a==b:
        al.append(2)
        continue
    if a<b:
        al.append(1)
        continue
    ans=10**10
    if b<10:
        for i in range(max(2,b),10):
            cost=i-b+ceil(log(a,i)+eps)
            # print(i,cost)
            ans=min(ans,cost)
    else:
        cost=ceil(log(a,b)+eps)
        ans=min(ans,cost)
    al.append(ans)
for a in al:print(a)


# for i in range(2,10):
    # print(log(100,i))