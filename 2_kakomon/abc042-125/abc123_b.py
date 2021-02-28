al=[int(input()) for _ in range(n)]
ans=10**10
for i in range(5):
    v=al[i]
    for j in range(5):
        if i!=j:
            v+=al[j]
            if al[j]%10!=0: v+=(10-al[j]%10)
    ans=min(ans,v)
print(ans)