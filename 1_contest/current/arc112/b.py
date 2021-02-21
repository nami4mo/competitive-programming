b,c=map(int, input().split())
if c==1:
    if b==0:
        print(1)
    else:
        print(2)
    exit()

if c==2:
    if b==0:
        print(2)
    else:
        print(3)
    exit()


if b>0:
    a1=b*(-1)
    a2=a1-(c-1)//2
    a3=max(0,b-(c-1)//2)*(-1)
    cnt=a3-a2+1

    d1=max(a3+1,b-c//2)
    d2=(c-2)//2+b
    cnt+=(d2-d1+1)

    print(cnt)

else:
    bleft_cnt=c//2+1

    bleft2=max(b+1, b*(-1)-(c-1)//2)
    bright=b*(-1)+(c-1)//2
    
    cnt=bleft_cnt+(bright-bleft2+1)
    print(cnt)