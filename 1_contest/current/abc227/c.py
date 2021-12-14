n=int(input())
ans=0
for i in range(1,10**4):
    rem = n//i # 10**6
    j=i
    while True:
        rem=n//(i*j)
        if rem < j:break
        ans+=(rem-j+1)
        j+=1
print(ans)