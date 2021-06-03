n,x=map(int, input().split())
if x==0:
    al=[100]*n
    print(1)
    print(*al)
    exit()

cnt=0
for i in range(n+1):
    if i*(i+1)//2>=x:
        cnt=i-1
        break
rem=x-cnt*(cnt+1)//2

if rem==0:
    al=[1]*cnt+[10**9]*(n-cnt)
    print(10**5)
    print(*al)
    exit()

k=10**5+(rem-1)
al=[1]*cnt+[10**5]+[10**9]*(n-cnt-1)
print(k)
print(*al)