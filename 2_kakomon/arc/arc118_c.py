n=int(input())
pl=[3,5,7,11]
cnt=0
MAX=10**4
rem=n-1
al=[]

for i in range(2,MAX+1,2):
    for p in pl:
        if i%p==0:
            cnt+=1
            break
print(cnt)

for i in range(2,MAX+1,2):
    for p in pl:
        if i%p==0:
            rem-=1
            al.append(i)
            break
    if rem==0:break
al.append(3*5*7*11)
print(*al)