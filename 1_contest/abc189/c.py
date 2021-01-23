n=int(input())
al=list(map(int, input().split()))

ans=0
for i in range(n):
    curr_min=10**10
    cnt=0
    for j in range(i,n):
        curr_min=min(curr_min,al[j])
        cnt+=1
        v=cnt*curr_min
        ans=max(ans,v)

print(ans)