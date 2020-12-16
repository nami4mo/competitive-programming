n,m=map(int, input().split())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))

# if n > m:
#     al,bl = bl,al

# a_del_cnt = 0
# b_del_cnt = 0
# for i in range(n):
#     if al[i] == bl[i]: continue
#     if al[i] != bl[i]:

def lcs_len(s1,s2):
    n1,n2 = len(s1),len(s2)
    dp = [ [0]*(n2+1) for _ in range(n1+1) ]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
            if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]+1
    return dp[-1][-1]

lcs = lcs_len(al,bl)
com = min(n,m)
print(com-lcs+abs(n-m))