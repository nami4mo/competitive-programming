ansl=[]
for _ in range(int(input())):
    n,m=map(int, input().split())
    for i in range(n):
        row=list(map(int, input().split()))
        for j in range(m):
            if (i+j)%2==0 and row[j]%2==0:row[j]+=1
            elif (i+j)%2==1 and row[j]%2==1:row[j]+=1
        ansl.append(row)

for row in ansl:print(*row)