import sys
input = sys.stdin.readline
from collections import deque
ansl=[]
for _ in range(int(input())):
    n,m=map(int, input().split())
    al=list(map(int, input().split()))
    bl=list(map(int, input().split()))
    cl=list(map(int, input().split()))
    cl=cl[::-1]
    used=-1
    need_cnt=0
    need={b:deque() for b in bl}
    ok={b:i for i,b in enumerate(bl)}
    for i in range(n):
        if al[i]!=bl[i]:
            need[bl[i]].append(i)
            need_cnt+=1
    ans=[]
    cnt=0
    # print('---')
    # print(need)
    for c in cl:
        if c in need and need[c]:
            poped=need[c].popleft()
            ans.append(poped+1)
            used=poped
            cnt+=1
        else:
            if used!=-1:
                ans.append(used+1)
            elif c in ok:
                ans.append(ok[c]+1)
                used=ok[c]
            else:
                ans=[]
                break
    if cnt==need_cnt:
        ansl.append(ans[::-1])
    else:
        # print('unko')
        ansl.append([])

for row in ansl:
    if row:
        print('YES')
        print(*row)
    else:
        print('NO')