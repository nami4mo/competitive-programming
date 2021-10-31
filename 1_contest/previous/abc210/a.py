n,a,x,y=map(int, input().split())
ans=0
if n<=a:
    print(x*n)
else:
    print(x*a+y*(n-a))
