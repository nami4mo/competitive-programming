def query(num):
    print(num,flush=True)
    res=input()
    if res=='Vacant':exit()
    return res

n=int(input())
al=['.']*n # f,m
l=0
r=n

al[0]=query(0)

for _ in range(19):
    mid=(l+r)//2
    ld=mid-l
    al[mid]=query(mid)
    if (ld%2==0 and al[l]!=al[mid]) or (ld%2==1 and al[l]==al[mid]):
        r=mid
        # print('r')
    else:
        l=mid
        # print('l')