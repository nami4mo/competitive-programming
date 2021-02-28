ansl=[]
for _ in range(int(input())):
    al=[]
    n=int(input())
    v=n

    if n<=16:
        for i in range(3,n):
            al.append((i,n))
        while v>1:
            al.append((n,2))
            v=(v-1)//2+1
        ansl.append(al)
        continue

    for i in range(3,n):
        if i!=16:
            al.append((i,n))
    v=n
    while v>1:
        al.append((n,16))
        v=(v-1)//16+1
    for j in range(4):
        al.append((16,2))
    ansl.append(al)

for row in ansl:
    print(len(row))
    for a,b in row:
        print(a,b)
# b=2*10**5
# for i in range(6):
#     b=(b-1)//16+1
#     print(b)