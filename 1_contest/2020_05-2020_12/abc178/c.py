MOD = 10**9+7
n = int(input())
all_cnt = pow(10,n,MOD)
no09 = pow(8,n,MOD)
yes09 = all_cnt-no09

no0 = pow(9,n,MOD)
yes0 = all_cnt-no0
yes9 = yes0

ans = yes0+yes9-yes09
print(ans%MOD)