from collections import deque
ansl = []
for _ in range(int(input())):
    n,q = map(int, input().split())
    s = input()
    for q_ in range(q):
        l,r = map(int, input().split())
        # print(l,r)
        l-=1
        r-=1
        # print(l,r,'-----')

        # sq = deque(list(s[l:r+1]))
        # prev_use = False
        # for i in range(n):
        #     if not sq: break
        #     if prev_use:
        #         prev_use = False
        #         continue
        #     if s[i] == sq[0]:
        #         sq.popleft()
        #         prev_use = True
        # if not sq:
        #     ansl.append('YES')
        # else:
        #     ansl.append('NO')    

        flag = False
        for i in range(l):
            # print(i,l,'---',s)
            if s[i] == s[l]:
                flag = True
                break
        # print(l,r,'----')
        if not flag:
            for i in range(r+1,n):
                # print(l,r)
                # if l == 2 and r == 4:
                #     # print(i,r,s,'aaaaa')
                if s[i] == s[r]:
                    flag = True
                    break
        if flag:
            ansl.append('YES')
        else:
            ansl.append('NO')

for a in ansl: print(a)