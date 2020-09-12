# https://atcoder.jp/contests/dp/tasks/dp_f?lang=ja

# get LCS length
def lcs_len(s1,s2):
    n1,n2 = len(s1),len(s2)
    dp = [ [0]*(n2+1) for _ in range(n1+1) ]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
            if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]+1
    return dp[-1][-1]

# get LCS string
def lcs_str(s1,s2):
    n1,n2 = len(s1),len(s2)
    dp = [ [0]*(n2+1) for _ in range(n1+1) ]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
            if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]+1
    ansr = []
    i,j = n1,n2
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]: i -= 1
        elif dp[i][j] == dp[i][j-1]: j -= 1
        else: 
            ansr.append(s1[i-1])
            i -= 1
            j -= 1
    ans = ansr[::-1]
    return ''.join(ans)


s1 = input()
s2 = input()
ans = lcs_str(s1,s2)
print(ans,flush=True)