n=int(input())
a,b,c=map(int, input().split())
ans=10**10
for i in range(10**4):
    for j in range(10**4):
        ab=a*i+b*j
        rem=n-ab
        if rem>=0 and rem%c==0:
            k=rem//c
            ans=min(ans,i+j+k)
print(ans)