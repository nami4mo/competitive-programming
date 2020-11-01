MOD = 998244353
a,b,c = map(int, input().split())
csum = c*(c+1)//2
bsum = b*(b+1)//2
asum = a*(a+1)//2
ans = asum*bsum*csum
ans %= MOD
print(ans)