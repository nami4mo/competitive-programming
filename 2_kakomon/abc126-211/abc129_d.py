def main():
    h,w = map(int, input().split())
    sl = []
    for _ in range(h):
        sl.append(list(input()))

    left_cnts = []
    for hi, row in enumerate(sl):
        curr_left_cnts = []
        curr_cnt = 0
        for i, s in enumerate(row):
            if s == '.':
                curr_left_cnts.append(curr_cnt)
                curr_cnt += 1
            else:
                curr_left_cnts.append(-1)
                curr_cnt = 0
        left_cnts.append(curr_left_cnts)


    right_cnts = []
    for hi, row in enumerate(sl):
        curr_right_cnts = []
        curr_cnt = 0
        for i, s in enumerate(row[::-1]):
            if s == '.':
                curr_right_cnts.append(curr_cnt)
                curr_cnt += 1
            else:
                curr_right_cnts.append(-1)
                curr_cnt = 0
        curr_right_cnts = curr_right_cnts[::-1]
        right_cnts.append(curr_right_cnts)


    sl_t = [list(x) for x in zip(*sl)]
    left_cnts_t = []
    for hi, row in enumerate(sl_t):
        curr_left_cnts = []
        curr_cnt = 0
        for i, s in enumerate(row):
            if s == '.':
                curr_left_cnts.append(curr_cnt)
                curr_cnt += 1
            else:
                curr_left_cnts.append(-1)
                curr_cnt = 0
        left_cnts_t.append(curr_left_cnts)


    right_cnts_t = []
    for hi, row in enumerate(sl_t):
        curr_right_cnts = []
        curr_cnt = 0
        for i, s in enumerate(row[::-1]):
            if s == '.':
                curr_right_cnts.append(curr_cnt)
                curr_cnt += 1
            else:
                curr_right_cnts.append(-1)
                curr_cnt = 0
        curr_right_cnts = curr_right_cnts[::-1]
        right_cnts_t.append(curr_right_cnts)


    ans = 0
    for hi in range(h):
        for wi in range(w):
            if sl[hi][wi] == '#':continue
            cnt = left_cnts[hi][wi] + right_cnts[hi][wi] + left_cnts_t[wi][hi] + right_cnts_t[wi][hi]
            ans = max(ans, cnt)

    print(ans+1)


if __name__ == "__main__":
    main()