from collections import deque

d = deque()
q = int(input())
q_l = []
for _ in range(q):
    query = list(map(str, input().split())) 
    q_l.append(query)

for query in q_l:
    if query[0] == '1':
        c = query[1]
        x = int(query[2])
        if len(d) == 0:
            d.append([c,x])
        elif d[-1][0] == c:
            d[-1][1] += x
        else:
            d.append([c,x])
    else:
        de = int(query[1])
        cnt_dir = {}
        while True:
            if len(d) == 0:
                break
            elif d[0][1] <= de:
                cnt_dir.setdefault(d[0][0], 0)
                cnt_dir[d[0][0]] += d[0][1]
                de -= d[0][1]
                d.popleft()
            else:
                cnt_dir.setdefault(d[0][0], 0)
                cnt_dir[d[0][0]] += de
                d[0][1] -= de
                break
        ans = 0
        for k, v in cnt_dir.items():
            ans += v**2
        print(ans)