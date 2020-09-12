s = input()
k = int(input())

cnt = 0
alps = 'abcdefghijklmnopqrstuvwxyz'
for alp in alps:
    inds = []
    for i,si in enumerate(s):
        if si == alp:
            inds.append(i)
    if inds:
        s_set = set()
        for ind in inds:
            for i in range(1,6):
                if ind+i <= len(s):
                    s_set.add(s[ind:ind+i])
        sl = list(s_set)
        if cnt + len(sl) >= k:
            sl.sort()
            print(sl[k-cnt-1])
            exit()
        else:
            cnt += len(sl)
