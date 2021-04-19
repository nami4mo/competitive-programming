a,b=map(int, input().split())
a,b=b,a
asum=a*(a+1)//2
bsum=b*(b+1)//2
if a<=b:
    d=bsum-asum
    ansl=[]
    for i in range(b):
        ansl.append(i+1)
    for i in range(a):
        ansl.append(-i-1)
    ansl[-1]-=d
else:
    d=asum-bsum
    ansl=[]
    for i in range(a):
        ansl.append(-i-1)
    for i in range(b):
        ansl.append(i+1)
    ansl[-1]+=d
print(*ansl)