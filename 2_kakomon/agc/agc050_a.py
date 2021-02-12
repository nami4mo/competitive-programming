n=int(input())
for i in range(1,n+1):
    a=(i*2)%n
    b=(i*2+1)%n
    if a==0:a=n
    if b==0:b=n
    print(a,b)