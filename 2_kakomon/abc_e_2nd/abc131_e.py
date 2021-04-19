n,k=map(int, input().split())
maxk=(n-1)*(n-2)//2
if maxk<k:
    print(-1)
    exit()

el=[]
for i in range(1,n):
    el.append((0,i))

rem=maxk-k
for i in range(1,n):
    if rem==0:break
    for j in range(i+1,n):
        el.append((i,j))
        rem-=1
        if rem==0:break


print(len(el))
for a,b in el:
    print(a+1, b+1)