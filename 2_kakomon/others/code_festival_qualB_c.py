s1=input()
s2=input()
s3=input()
n=len(s1)//2

from collections import Counter
c1=Counter(s1)
c2=Counter(s2)
c3=Counter(s3)

dp=[[False]*(n+1) for _ in range(27)]
dp[0][0]=True
ALPs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i,a in enumerate(ALPs):
    if c1[a]+c2[a]<c3[a]:
        print('NO')
        exit()
    right=min(c1[a],c3[a])
    left=max(0,c3[a]-c2[a])
    cumsum=[0]
    cs=0
    for j in range(n+1):
        if dp[i][j]:cs+=1
        cumsum.append(cs)
    for j in range(n+1):
        true_cnt=cumsum[max(0,j+1-left)]-cumsum[max(j-right,0)]
        if true_cnt>0:
            dp[i+1][j]=True

if dp[-1][n]:print('YES')
else:print('NO')
