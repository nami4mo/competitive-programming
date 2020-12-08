from collections import deque


n=int(input())
pl=list(map(int, input().split()))

cnt=0
for i in range(n):
    if i+1 == pl[i]:
        print(-1)
        exit()
    diff = i+1-pl[i]
    cnt += diff
if cnt != 0:
    print(-1)
    exit()


swaped = 0
waited = [10**10]*n
# wq = deque()
ansl = []
used = [False]*(n+1)
for i in range(n-1):
    # print(pl)
    if pl[i] > pl[i+1]:
        pl[i],pl[i+1] = pl[i+1],pl[i]
        ansl.append(i+1)
        used[i+1] = True
        swaped += 1
        for j in range(i,0,-1):
            if pl[j-1] > pl[j]:
                if used[j]:
                    print(-1)
                    exit()
                pl[j-1], pl[j] = pl[j], pl[j-1]
                ansl.append(j)
                used[j] = True
                swaped += 1
            else:
                break

for i in range(n):
    if i+1 != pl[i]:
        print(-1)
        exit()
else:
    if swaped == n-1:
        for a in ansl:
            print(a)
    else:
        print(-1)
