import bisect
import sys
input = sys.stdin.readline

def main():
    a,b,q = map(int, input().split())

    sl = [int(input()) for _ in range(a)]
    tl = [int(input()) for _ in range(b)]
    xl = [int(input()) for _ in range(q)]

    for x in xl:
        ans = 10**11

        curr_dist = 0
        ind_s = bisect.bisect_left(sl, x)
        ind_t = bisect.bisect_left(tl, x)
        
        for next_s in [ind_s, ind_s-1]:
            if 0 <= next_s < a:
                curr_dist = abs(x-sl[next_s])
                curr_pos = sl[next_s]
                ind_t2 = bisect.bisect_left(tl, curr_pos)
                if ind_t2 == 0:
                    curr_dist += abs(tl[0] - curr_pos)
                elif ind_t2 == b:
                    curr_dist += abs(tl[b-1] - curr_pos)
                else:
                    curr_dist += min( abs( tl[ind_t2-1] - curr_pos), abs(tl[ind_t2]-curr_pos))
                ans = min(curr_dist, ans)


        for next_t in [ind_t, ind_t-1]:
            if 0 <= next_t < b:
                curr_dist = abs(x-tl[next_t])
                curr_pos = tl[next_t]
                ind_s2 = bisect.bisect_left(sl, curr_pos)
                if ind_s2 == 0:
                    curr_dist += abs(sl[0] - curr_pos)
                elif ind_s2 == a:
                    curr_dist += abs(sl[a-1] - curr_pos)
                else:
                    curr_dist += min( abs( sl[ind_s2-1] - curr_pos), abs(sl[ind_s2]-curr_pos))
                ans = min(curr_dist, ans)

        print(ans)


if __name__ == "__main__":
    main()