s=input()
cho='chokudai'
for i in range(len(cho)):
    s=s.replace(cho[i],str(i))

MOD=10**9+7
dp=[0]*8
for si in s:
    if not '0'<=si<='9': continue
    sii=int(si)
    if sii==0:
        dp[0]+=1
    else:
        dp[sii]+=dp[sii-1]
        dp[sii]%=MOD
print(dp[7])