from collections import deque
ansl = []
for _ in range(int(input())):
    n = int(input())
    al = list(map(int, input().split()))
    lockl = list(map(int, input().split()))

    free = []
    locked = []
    for a, l in zip(al,lockl):
        if l == 0: free.append(a)
        else: locked.append(a)

    free.sort(reverse=True)
    fq = deque(free)
    lq = deque(locked)
    ans = []
    for i in range(n):
        if lockl[i] == 0:
            ans.append(fq.popleft())
        else:
            ans.append(lq.popleft())
    ansl.append(ans)

for ans in ansl:
    print(*ans)

