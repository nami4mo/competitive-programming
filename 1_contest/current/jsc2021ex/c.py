a,b=map(int, input().split())

MAX=2*10**5+1
ans=1
for i in range(MAX,0,-1):
    if a%i==0:
        l=a
    else:
        l=a+(i-a%i)
    r=l+i
    # if i==34:print(l,r)
    if a<=l<=b and a<=r<=b:
        print(i)
        exit()
