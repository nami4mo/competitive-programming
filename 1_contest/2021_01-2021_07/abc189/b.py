n,x=map(int, input().split())
x*=100
vol=0
for i in range(n):
    v,p=map(int, input().split())
    vol+=v*p
    if vol>x:
        print(i+1)
        exit()
print(-1)