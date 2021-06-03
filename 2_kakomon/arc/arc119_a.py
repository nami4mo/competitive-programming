n=int(input())
ans=10**18
for b in range(100):
    if pow(2,b)>n:
        break

    a=n//pow(2,b)
    c=n-a*pow(2,b)
    ans=min(ans,a+b+c)
print(ans)