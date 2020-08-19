from bisect import bisect_left, bisect_right

n = int(input())
al = list(map(int, input().split()))

al2 = [ [] for _ in range(20)]
for a in al:
    for i in range(20):
        if a&(1<<i) > 0:
            al2[i].append(1)
        else:
            al2[i].append(0)

al2_cum = []
for i in range(20):
    cum = 0
    cumsum = [0]
    for a in al2[i]:
        cum += a
        cumsum.append(cum)
    al2_cum.append(cumsum)

# print(al2)
# print(al2_cum)
ans = 0
for i in range(n+1):
    curr_maxind = 0
    for j in range(20):
        curr_cum = al2_cum[j]
        curr_1_cnt = curr_cum[i]
        if curr_1_cnt <= 1:
            continue
        else:
            ind = bisect_left(curr_cum, curr_1_cnt-1)
            curr_maxind = max(curr_maxind,ind)
    ans += (i-curr_maxind)

print(ans)