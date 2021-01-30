n=int(input())
n*=2

MAX=6*(10**6)
ans=0
for i in range(1,MAX):
    if i*i > n: break
    if n%i!=0: continue
    r=n//i
    if i%2==0 and r%2==1: 
        # print(i)
        ans+=1
    if i%2==1 and r%2==0: 
        # print(i)
        ans+=1

    if i!=r:
        if i%2==0 and r%2==1: 
            ans+=1
        if i%2==1 and r%2==0: 
            ans+=1

print(ans)