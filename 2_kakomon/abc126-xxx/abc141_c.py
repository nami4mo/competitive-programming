n,k,q = map(int, input().split())

a_cnt = [0]*n
for _ in range(q):
    a = int(input()) - 1
    a_cnt[a] += 1


for a in a_cnt:
    if k - (q-a) > 0:
        print('Yes')
    else:
        print('No')