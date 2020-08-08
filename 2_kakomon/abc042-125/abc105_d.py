n,m = map(int, input().split())
A = list(map(int, input().split()))

rem_cnts = {0:0}
curr_sum_rem = 0
for a in A:
    curr_sum_rem += a
    curr_sum_rem%=m
    rem_cnts.setdefault(curr_sum_rem,0)
    rem_cnts[curr_sum_rem] += 1

ans = 0
for cnt in rem_cnts.values():
    ans += cnt*(cnt-1)//2
ans += rem_cnts[0]

print(ans)