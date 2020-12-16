n,m=map(int, input().split())
# gl=[[] for _ in range(n)]
gl=[]
for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    # gl[a].append(b)
    gl.append((a,b))

dp=[0]*(2**n)
dp[0]=1
for i in range(2**n):
    used = set()
    for j in range(n):
        if (i>>j)%2==1: used.add(j)
    in_cnts = [0]*n
    for a,b in gl:
        if a in used:continue
        in_cnts[b]+=1
    for j in range(n):
        if j in used:continue
        if in_cnts[j] > 0: continue
        dp[i|(2**j)] += dp[i]

print(dp[-1])
in_c