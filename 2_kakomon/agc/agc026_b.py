from math import gcd
ansl=[]
for _ in range(int(input())):
    a,b,c,d=map(int, input().split())
    if b>d or a-b<0:
        ansl.append('No')
        continue
    if b-1<=c:
        ansl.append('Yes')
        continue

    g=gcd(b,d)
    left=c+1-a%b
    cnt=b-c-1
    left_rem=left%g
    if left_rem==0:
        ansl.append('No')
    else:
        need_cnt=g-left_rem+1
        if cnt>=need_cnt:
            ansl.append('No')
        else:
            ansl.append('Yes')

for a in ansl:print(a)