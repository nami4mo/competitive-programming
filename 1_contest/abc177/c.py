n = int(input())
al = list(map(int, input().split()))
curr_sum = sum(al)
ans = 0
MOD = 10**9+7
for i,a in enumerate(al):
    curr_sum -= a
    ans += curr_sum*a
    ans%=MOD

print(ans)