
p2=[]
for i in range(62):
    p2.append(pow(2,i))

allps=[1]
for i in range(1,22):
    allps.append(allps[-1]*i)
# print(allps)

def solve(n,k):
    if n==1:
        return 1,1
    cp=n-2
    cnt=1
    csum=0
    for i in range(62):
        # print(cp)
        if cp<0:break
        if cp>=62:break
        if csum+p2[cp]>=k:break
        else:
            cnt+=1
            csum+=p2[cp]
            cp-=1
    return cnt, csum
    
# ansl=[]

for _ in range(int(input())):
    n,k=map(int, input().split())
    orig_n=n
    if n<100 and pow(2,n-1)<k:
        # ansl.append([-1])
        print(-1)
        continue
    rem=k
    cp=n-2
    cmax=0
    al=[]
    ccc=0
    while rem>1:
        cnt,csum=solve(n,rem)
        n-=cnt
        rem-=csum
        cmax+=cnt
        for i in range(cnt):
            ccc+=1
            # al.append(cmax-i)
            print(cmax-i,end=' ')
        
    # cnt=orig_n-len(al)
    cnt=orig_n-ccc
    cmax+=1
    for i in range(cnt):
        # al.append(cmax+i)
        print(cmax+i, end=' ')
    print()
    # ansl.append(al)
    # print(*al,flush=True)

# for row in ansl:
#     print(*row)