def ctoi(c):
    return ord(c)-ord('a')

s=input()
n=len(s)
alps = 'abcdefghijklmnopqrstuvwxyz' # string.ascii_lowercase

# dp_same=[[0]*26 for _ in range(n)]
# dp_diff=[[0]*26 for _ in range(n)]

# if s[0]==s[1] and s[1]!=s[2]:
#     dp_same[2][ctoi(s[0])]=1
#     dp_diff[2][ctoi(s[2])]
# else:
#     dp_diff[1][ctoi(s[0])]=1

first=-1
for i in range(n-1):
    if s[i]==s[i+1]:
        first=i
        break
if first==-1:
    print(0)
    exit()

s=s[i:]
n=len(s)
if n==2:
    print(0)
    exit()

dp=[[-1]*26 for _ in range(26)]
dp[ctoi(s[0])][ctoi(s[1])]=1
dp[ctoi(s[1])][ctoi(s[2])]=0

from copy import copy

for i in range(3,n):
    dp2=[[-1]*26 for _ in range(26)]
    ssi=s[i]
    si=ctoi(ssi)
    for cc1 in alps:
        for cc2 in alps:
            c1=ctoi(cc1)
            c2=ctoi(cc2)
            if dp[c1][c2]==-1:continue
            if c1==c2:
                if c2==si:
                    dp2[c2][c2]=max(dp2[c2][c2],dp[c2][c2])
                else:
                    dp2[c2][si]=max(dp2[c2][si],dp[c2][c2])
                    dp2[c2][c2]=max(dp2[c2][c2], dp[c2][c2]+1)
            else:
                dp2[c2][si]=max(dp2[c2][si],dp[c1][c2])
    dp=copy(dp2)

ans=0
for i in range(26):
    for j in range(26):
        ans=max(ans,dp[i][j])
print(ans)

# for i in range(2,n):
#     si=s[i]
#     for c in alps:
#         ci=ctoi(c)
#         if si==c:
#             dp_same[i][ci]=dp_same[i-1][ci]
#             dp_same[i][ci]=max(dp_diff[i-1][ci], dp_same[i][ci])
#         else:
#             dp_same[i][ci]=dp_same[i-1]+1
#             dp_diff[i][ci]=max(dp_diff[i-1][ci], max(dp_diff[i-1])) # todo

        
