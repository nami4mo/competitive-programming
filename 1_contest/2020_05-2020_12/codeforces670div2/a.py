for _ in range(int(input())):
    n = int(input())
    al = list(map(int, input().split()))
    al.sort()
    cntl = []
    prev = al[0]
    cnt = 1
    for a in al[1:]:
        if prev == a: cnt+=1
        else:
            cntl.append((prev,cnt))
            cnt = 1
            prev = a
    cntl.append((prev,cnt))


    one_end = False
    ans1 = -1
    ans2 = -1
    # print(cntl)
    for i, (a,cnt) in enumerate(cntl):
        if a == i:
            if cnt >= 2:
                # i += 1
                pass
            else:
                if not one_end:
                    ans1 = i
                    one_end = True
                    # i += 1
                else:
                    pass
        else:
            if ans1 == -1: ans1 = i
            ans2 = i
            break
    else:
        if ans1 == -1: ans1 = max(al)+1
        if ans2 == -1: ans2 = max(al)+1
    print(ans1+ans2)

    # for i, (a,cnt) in enumerate(cntl):
    #     if a == i:
    #         if cnt >= 2:
    #             # i += 1
    #             pass
    #         else:
    #             if not one_skip:
    #                 ans1 = i
    #                 one_skip = True
    #                 # i += 1
    #             else:
    #                 ans2 = i
    #                 break
    #     else:
    #         if ans1 == -1: ans1 = i
    #         ans2 = i
    #         break
    # else:
    #     if ans1 == -1: ans1 = max(al)+1
    #     if ans2 == -1: ans2 = max(al)+1
    # print(ans1+ans2)
    # print(ans1,ans2)




