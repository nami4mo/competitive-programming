h,w=map(int, input().split())

if h==3 and w==3:
    print('Yes')
    print('225')
    print('555')
    print('225')
    exit()

c=h*w
if h==1 or w==1:
    if not c%7 in [0,2,5]:
        print('No')
        exit()

    if c%7==0:
        ansl=[]
        for _ in range(c//7):
            ansl.extend([2,2,5,5,5,5,5])

    elif c%7==2:
        ansl=[2,2]
        for _ in range(c//7):
            ansl.extend([5,5,5,5,5,2,2])

    elif c%7==5:
        ansl=[5,5,5,5,5]
        for _ in range(c//7):
            ansl.extend([2,2,5,5,5,5,5])

    print('Yes')
    if h==1:
        ans=''
        for a in ansl:ans+=str(a)
        print(ans)
    else:
        for a in ansl:print(a)

elif h==2:
    if w%7 not in [0,1,6]:
        print('No')
        exit()
    print('Yes')

    ans1=''
    if w%7==6: ans1+='555255'
    for _ in range(w//7):
        ans1+='2555255'
    if w%7==1: ans1+='2'
    print(ans1)

    ans2=''
    if w%7==6: ans2+='552555'
    for _ in range(w//7):
        ans2+='2552555'
    if w%7==1: ans2+='2'
    print(ans2)

elif w==2:
    if h%7 not in [0,1,6]:
        print('No')
        exit()
    ansl=['22','55','55','52','25','55','55']
    print('Yes')
    rem=h
    if h%7==6:
        rem-=6
        for i in range(6):
            print(ansl[i+1])
    for i in range(rem):
        print(ansl[i%7])
else:
    print('No')