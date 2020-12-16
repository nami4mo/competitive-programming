from math import sqrt
n,d=map(int, input().split())
xl=[]
for _ in range(n):
    x=list(map(int, input().split()))
    xl.append(x)

ans=0
for i in range(n):
    for j in range(i+1,n):
        d2 = 0
        for k in range(d):
            d2 += (xl[i][k]-xl[j][k])**2
        if sqrt(d2).is_integer():ans+=1

print(ans)