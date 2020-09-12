n = int(input())
v = 1
MOD = 10**9+7
for i in range(1,n+1):
    v *= i
    v%=MOD

v -= pow(2,n-1,MOD)
v%=MOD
print(v)