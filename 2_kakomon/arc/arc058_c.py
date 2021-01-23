n,x,y,z=map(int, input().split())
xyz=x+y+z
MOD=10**9+7
dp=[0]*(2**xyz)
dp[0]=1

check_bits=(1<<(z-1))|(1<<(y+z-1))|(1<<(x+y+z-1))
# print(str(bin(check_bits))[2:])

MAX=2**xyz
ans=0
for i in range(n):
    new_dp=[0]*(2**xyz)
    new_dp[0]=0
    # print('--',i)
    for bits in range(MAX):
        if dp[bits]==0:continue
        # print(str(bin(bits))[2:])
        for a in range(1,11):
            newbits=(bits<<(a))
            newbits|=(1<<(a-1))
            newbits&=(MAX-1)
            if check_bits&newbits!=check_bits:
                new_dp[newbits]+=dp[bits]
                new_dp[newbits]%=MOD
    dp=new_dp[:]

ans=pow(10,n,MOD)
for bits in range(MAX):
    # if check_bits&bits==check_bits:
    ans-=dp[bits]
    ans%=MOD
# ans=u-ans
# print(ans%MOD)
print(ans)