for _ in range(int(input())):
    n,k = map(int, input().split())
    s = input()
    sl = list(s)

    # hatena_len = 0
    # sl = []
    # for i in range(n):
    #     if s[i] == '?': 
    #         hatena_len += 1
    #         if hatena_len > k+1: 
    #             continue
    #     else: hatena_len = 0
    #     sl.append(s[i])
    # n = len(sl)

    hatena_p = []
    for i in range(n-k):
        poped = sl[i]
        new = sl[i+k]
        if poped == '?' and new == '?':
            hatena_p.append((i,i+k))
        elif poped == new:
            pass
        elif poped == '0' and new == '1':
            print('NO')
            break
        elif poped == '1' and new == '0':
            print('NO')
            break
        elif poped == '?':
            sl[i] = new
        elif new == '?':
            sl[i+k] = poped
    else:
        for pf,pb in hatena_p[::-1]:
            sl[pf] = sl[pb]
        # print(sl)
        cnt_zero = 0
        cnt_one = 0
        for i in range(k):
            if sl[i] == '0': cnt_zero += 1
            elif sl[i] == '1': cnt_one += 1
        if cnt_zero > k//2 or cnt_one > k//2:
            print('NO')
        else:
            print('YES')


