for _ in range(int(input())):
    n = int(input())
    al = list(map(int, input().split()))
    ans = 0
    l = 1
    # r = n-1
    for i in range(n-1):
        if al[i] > 0:
            al[i+1] += al[i]
            al[i] = 0
    print(al[-1])

            # rem = al[i]
            # while True:
            #     if l < n and al[l] < 0:
            #         if rem < al[l]*(-1):
            #             al[l] += rem
            #             break
            #         else:
            #             rem += al[l]
            #             al[l] = 0
            #             l += 1
                



    # for i in range(n-1):
    #     if al[i] < 0:
    #         ans -= al[i]
    #         rem = -al[i]
    #         # if al[l] > 0:
    #         while True:
    #             if al[r] > rem:
    #                 al[r] -= rem
    #                 break
    #             else:
    #                 if al[r] > 0:
    #                     rem -= al[r]
    #                     al[r] = 0
    #                 while True:
    #                     r-=1
    #                     if al[r] > 0 or r == 0: break
    #             if rem == 0:
    #                 break
    #         # r = max(i+1,l)

    #     elif al[i] > 0:
    #         # ans -= a[i]
    #         rem = al[i]
    #         # if al[l] > 0:
    #         while True:
    #             if (-1)*al[l] > rem:
    #                 al[l] += rem
    #                 break
    #             else:
    #                 if al[l] < 0:
    #                     rem += al[l]
    #                     al[l] = 0
    #                 while True:
    #                     l+=1
    #                     if l >= n-1 or al[l] < 0: break
    #             if rem == 0:
    #                 break
    #         l = max(i+1,l)
    # print(ans)

    # for i in range(n-1):
    #     a1 = al[i]
    #     a2 = al[i+1]
    #     if a1 > 0:
    #         al[i] = 0
    #         al[i+1] += a1
    #     else:
    #         ans += (-1)*a1
    #         al[i] = 0
    #         al[i+1] += a1
    #     print(al, ans)
    # break
    # print(ans)

        
        