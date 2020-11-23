from collections import deque

h,w = map(int, input().split())
al = [input() for _ in range(h)]

g = [ [] for _ in range(h*w+26)]
s = -1
goal = -1

for hi in range(h):
    for wi in range(w):
        curr = al[hi][wi]
        if curr == '#': continue

        u = hi*w+wi
        if curr == 'S':
            s = hi*w+wi
        elif curr == 'G':
            goal = hi*w+wi
        elif curr != '.':
            super_v = ord(curr)-ord('a') + h*w
            # g[super_v].append((u,0))
            # g[u].append((super_v,1))
            g[super_v].append(u)
            g[u].append(super_v)

        if hi+1 < h and al[hi+1][wi] != '#':
            v = (hi+1)*w+wi
            # g[u].append((v,1))
            # g[v].append((u,1))
            g[u].append(v)
            g[v].append(u)
        if wi+1 < w and al[hi][wi+1] != '#':
            v = hi*w+wi+1
            # g[u].append((v,1))
            # g[v].append((u,1))
            g[u].append(v)
            g[v].append(u)

visited = [-1]*(h*w+26)
q = deque([s])
visited[s] = 0
ans = -1
while q:
    poped = q.popleft()
    if poped == goal:
        ans = visited[goal]
        break
    for v in g[poped]:
        if visited[v] != -1: continue
        if v >= h*w: cost = 0
        else: cost = 1
        visited[v] = visited[poped]+cost
        if cost == 0:
            q.appendleft(v)
        else:
            q.append(v)

print(ans)