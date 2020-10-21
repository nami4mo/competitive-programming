from bisect import bisect_left, bisect_right

n = int(input())
rems = list(map(int, input().split()))
rems.sort()
gots = [rems[-1]]
rems.pop()

for i in range(n):
    r = len(rems)-1
    new_gots = []
    next_rem_inds = [True]*len(rems)
    for g in gots:
        ind = bisect_left(rems, g)-1
        if ind < 0 or len(rems) <= ind or r < 0:
            print('No')
            exit()
        if ind > r: 
            ind = r
        new_gots.append(rems[ind])
        next_rem_inds[ind] = False
        r = ind-1
    for g in new_gots:
        gots.append(g)
    new_rems = []
    for i,v in enumerate(rems):
        if next_rem_inds[i]: new_rems.append(v)
    rems = new_rems[:]
    gots.sort(reverse=True)
    # rems.sort()

print('Yes')