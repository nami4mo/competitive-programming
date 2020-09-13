from collections import deque, Counter
from bisect import bisect_left, bisect_right


# [1, 2, 2, 2, 5]
# [1, 3, 3, 4, 5]
n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

c = Counter(al)
cnt_mosts = c.most_common()
avals = []
for val,cnt in cnt_mosts:
    r = bisect_right(al, val) - 1
    l = bisect_left(al, val)
    avals.append((val,l,r))


exist = [0]*(n+1)
for a in al:
    exist[a] = True

bl.sort(reverse=True)
c = Counter(bl)
cnt_mosts = c.most_common()
bl.sort()

# print(cnt_mosts)

bvals = []
for val,cnt in cnt_mosts:
    r = bisect_right(bl, val) - 1
    l = bisect_left(bl, val)
    bvals.append((val,r-l+1))
    # print(val, r-l+1)

hayame = deque([])
always = deque([])
b_cnt = [-1]*(n+1)
# for b in bl:
for b, cnt in bvals:
    if exist[b]:
        for _ in range(cnt):
            hayame.append(b)
            b_cnt[b] = cnt
    else:
        for _ in range(cnt):
            always.append(b)
            b_cnt[b] = cnt

# print(hayame)
# print(always)

# # bcnt = [0]
# print(b_cnt)
aq = deque(avals)
skip = [False]*(n+1)
ansl = [-1]*n
# for a, l, r in avals:
while aq:
    a,l,r = aq[0]
    if b_cnt[a]==0 and not skip[a]:
        poped = aq.popleft()
        aq.append(poped)
        skip[a] = True
        # print('skip')
        continue
    aq.popleft()
    for i in range(l,r+1):
        while hayame and hayame[0] == a:
            hayame.popleft()
            always.append(a)
        if hayame:
            poped = hayame.popleft()
            # ansl.append(poped)
            ansl[i] = poped
            b_cnt[poped] -= 1
        elif always and always[0] != a:
            poped = always.popleft()
            # ansl.append(poped)
            ansl[i] = poped
            b_cnt[poped] -= 1
        else:
            print('No')
            # print(ansl)
            exit()
    # print('--')
    # print(hayame)
    # print(always)

print('Yes')
print(*ansl)
        