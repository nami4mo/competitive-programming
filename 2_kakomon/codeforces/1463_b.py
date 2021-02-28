ansl=[]
for _ in range(int(input())):
    n=int(input())
    al=list(map(int, input().split()))
    bl1=[]
    bl2=[]
    s1,s2=0,0
    for i in range(n):
        if i%2==0:
            bl1.append(1)
            bl2.append(al[i])
            s1+=abs(al[i]-1)
        else:
            bl2.append(1)
            bl1.append(al[i])
            s2+=abs(al[i]-1)
    if s1<s2:
        ansl.append(bl1)
    else:
        ansl.append(bl2)

for row in ansl:
    print(*row)
