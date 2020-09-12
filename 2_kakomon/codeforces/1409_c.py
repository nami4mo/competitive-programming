t=int(input())
for _ in range(t):
    n,x,y = map(int, input().split())
    d = y-x
    ansl = []
    ansv = 10**9
    for i in range(1,d+1):
        if d%i != 0: continue
        v = y
        to_front = True
        curr_ansl = [v]
        for _ in range(n-1):
            if to_front:
                if v-i > 0:
                    v -= i
                    curr_ansl.append(v)
                else:
                    to_front = False
                    v = y+i
                    curr_ansl.append(v)
            else:
                v += i
                curr_ansl.append(v)
        if min(curr_ansl) > x:
            continue

        mmax = max(curr_ansl)
        if mmax < ansv:
            ansv = mmax
            ansl = curr_ansl[:]
    ansl.sort()
    print(*ansl)
            