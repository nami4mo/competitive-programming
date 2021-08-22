from collections import deque

n,k = map(int, input().split())
al = list(map(int, input().split()))

val_cnt = {}
val_cnt[0] = 1
val_q = deque([0])
if k == 1:
    print(0)
    exit()

ans = 0
curr_sum = 0
for i in range(n):
    curr_sum += al[i]
    curr_sum %= k
    val = (curr_sum - (i+1))%k
    val_cnt.setdefault(val,0)
    ans += val_cnt[val]
    val_cnt[val] += 1
    val_q.append(val)
    if len(val_q) >= k:
        poped = val_q.popleft()
        val_cnt[poped] -= 1

print(ans)