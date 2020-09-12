from heapq import heappop, heappush

q = int(input())
ans = 0

mid_1 = 0
mid_2 = 0
mid = 0
left_q = []
right_q = []
left_sum = 0
right_sum = 0
const_b = 0
ansl = []

first_flag = True
double_mid = False
for _ in range(q):
    row = list(input().split())
    if row[0] == '2':
        half_n = len(left_q)
        if double_mid:
            q_left_sum = mid_1*half_n - left_sum
            q_right_sum = right_sum - mid_1*half_n
            ans_v = q_left_sum + q_right_sum + (mid_2-mid_1) + const_b
            ans_x = mid_1
            ansl.append((ans_x, ans_v))
        else:
            q_left_sum = mid*half_n - left_sum
            q_right_sum = right_sum - mid*half_n
            ans_v = q_left_sum + q_right_sum + const_b
            ans_x = mid
            ansl.append((ans_x, ans_v))
    
    else:
        a,b = int(row[1]), int(row[2])
        const_b += b

        if first_flag:
            mid = a
            first_flag = False

        elif double_mid:
            double_mid = False
            if a <= mid_1:
                heappush(left_q, a*(-1))
                left_sum += a
                heappush(right_q, mid_2)
                right_sum += mid_2
                mid = mid_1
            elif a >= mid_2:
                heappush(left_q, mid_1*(-1))
                left_sum += mid_1
                heappush(right_q, a)
                right_sum += a
                mid = mid_2
            else:
                heappush(left_q, mid_1*(-1))
                left_sum += mid_1
                heappush(right_q, mid_2)
                right_sum += mid_2
                mid = a
            # print(left_q, mid, right_q)
            # print(left_sum, right_sum)


        else:
            double_mid = True
            if a <= mid:
                heappush(left_q, a*(-1))
                left_sum += a
                mid_1 = heappop(left_q)*(-1)
                left_sum -= mid_1
                mid_2 = mid
            else:
                heappush(right_q, a)
                right_sum += a
                mid_1 = mid
                mid_2 = heappop(right_q)
                right_sum -= mid_2
            # print(left_q, mid_1, mid_2, right_q)
            # print(left_sum, right_sum)



for ax,av in ansl:
    print(ax,av)