n=int(input())
al=[list(map(int, input().split())) for _ in range(n)]

dp=[0]*(1<<n)
for i in range(1<<n):
    gs=[]
    for bit in range(n):
        if i&(1<<bit) > 0: gs.append(bit)
    for j1 in range(len(gs)):
        for j2 in range(j1,len(gs)):
            dp[i]+=al[gs[j1]][gs[j2]]

    
    bits = i
    while True:  
        bits = (bits-1) & i
        comp = bits ^ i
        if bits <= i//2: break
        dp[i]=max(dp[i], dp[bits]+dp[comp])

print(dp[-1])
# print(dp)