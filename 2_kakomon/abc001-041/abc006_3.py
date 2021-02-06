n,m=map(int, input().split())
for c in range(2*10**5):
    b=m-2*n-2*c
    a=n-b-c
    if a>=0 and b>=0:
        print(a,b,c)
        break
else:
    print(-1,-1,-1)