from collections import Counter
n,m=map(int, input().split())
al=list(map(int, input().split()))
c=Counter(al)

rems_p_cnt = [0]*m
rems_single_cnt = [0]*m
rems_cnt = [0]*m
for i in range(1,10**5+1):
    cnt = c[i]
    rems_p_cnt[i%m] += cnt//2
    rems_single_cnt[i%m] += cnt%2
    rems_cnt[i%m] += cnt

# for i in range(m):
ans=0
ans+=(rems_cnt[0]//2)
if m%2==0:
    ans+=(rems_cnt[m//2]//2)

# print(ans)
# print(rems_p_cnt)
# print(rems_single_cnt)
# print(rems_cnt)
for i in range(1,m//2+1):
    if m%2==0 and i==m//2: continue
    j = m-i
    pair = min(rems_cnt[i],rems_cnt[j])
    ans += pair

    if pair > rems_single_cnt[i]:
        diff = pair-rems_single_cnt[i]
        rems_p_cnt[i]-=(diff+1)//2
    if pair > rems_single_cnt[j]:
        diff = pair-rems_single_cnt[j]
        rems_p_cnt[j]-=(diff+1)//2

    ans += rems_p_cnt[i]
    ans += rems_p_cnt[j]

# print(rems_p_cnt)

print(ans)