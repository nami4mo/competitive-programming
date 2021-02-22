ansl=[]
for _ in range(int(input())):
    n=int(input())
    al=[]
    if n%2==0:
        for i in range(n//2-1):
            al.append(1)
        al.append(0)
        for i in range(n//2-1):
            al.append(-1)
    else:
        for i in range(n//2):
            al.append(1)
        for i in range(n//2):
            al.append(-1)
    ans=[]
    for i in range(n):
        for j in range(n-1-i):
            ans.append(al[j])
    ansl.append(ans)

for row in ansl:print(*row)