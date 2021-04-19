r,x,y=map(int, input().split())
d2=x**2+y**2

if r**2==d2:
    print(1)
    exit()
for i in range(2,10**7):
    r2=(i*r)**2
    if r2>=d2:
        print(i)
        exit()
