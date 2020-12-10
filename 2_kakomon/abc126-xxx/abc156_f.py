k,q=map(int, input().split())
dl=list(map(int, input().split()))

ansl=[]
for _ in range(q):
    n,x,m=map(int, input().split())
    loop_cnt = (n-1)//k
    loop_rem = (n-1)%k

    loop_sum = 0
    loop_same = 0
    rems_sum = 0
    rems_same = 0
    for i in range(k):
        loop_sum += dl[i]%m
        if i < loop_rem: 
            rems_sum += dl[i]%m

        if dl[i]%m==0:
            loop_same += 1
            if i < loop_rem: 
                rems_same += 1

    sums = loop_sum*loop_cnt + rems_sum + x%m
    down_cnt = sums//m 
    same_cnt = loop_cnt*loop_same + rems_same
    ans = n-1 - down_cnt - same_cnt
    ansl.append(ans)
    # print(down_cnt, same_cnt)

for a in ansl:print(a)
