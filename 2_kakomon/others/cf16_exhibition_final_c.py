n=int(input())
al=[int(input()) for _ in range(n)]

xsum=0
for a in al: xsum^=a

lsbs=set()
for a in al:
    lsb=a&(-a)
    lsbs.add(lsb)

ans=0
for i in range(30,-1,-1):
    if (xsum>>i)&1:
        if (1<<i) not in lsbs:
            print(-1)
            exit()
        xsum^=((1<<i)*2-1)
        ans+=1

if xsum==0:print(ans)
else: print(-1)
