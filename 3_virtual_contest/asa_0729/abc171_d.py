n = int(input())
al = list(map(int, input().split()))

num_cnt = {}
c_sum = 0
for a in al:
    num_cnt.setdefault(a,0)
    num_cnt[a] += 1
    c_sum += a

ans = []
q = int(input())

for _ in range(q):
    b,c = map(int, input().split())
    num_cnt.setdefault(b,0)
    num_cnt.setdefault(c,0)
    diff = num_cnt[b]*c - num_cnt[b]*b

    num_cnt[c] += num_cnt[b]
    num_cnt[b] = 0
    c_sum += diff
    ans.append(c_sum)

for a in ans:
    print(a)