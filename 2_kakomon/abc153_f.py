from collections import deque

n,d,a = map(int, input().split())
xhl = []
for _ in range(n):
    x,h = map(int, input().split())
    cnt = (h-1)//a + 1
    xhl.append((x,cnt))

xhl.sort()

attack_q = deque([])
attack_sum = 0
ans = 0
for x,h in xhl:
    # print('----',((x,h)))
    # print(attack_q)
    # print(attack_sum)
    while attack_q and attack_q[0][0] < x:
        poped_cnt = attack_q.popleft()[1]
        attack_sum -= poped_cnt
    # print(attack_q)
    # print(attack_sum)
    rem = h-attack_sum
    if rem <= 0:
        continue
    attack_sum += rem
    ans += rem
    attack_q.append((x+2*d, rem))
    # print(rem)

print(ans)
# print(xhl)