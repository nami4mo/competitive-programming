n,k = map(int, input().split())
pl = [0] + list(map(int, input().split()))
cl = [0] + list(map(int, input().split()))

ans = (10**18)*(-1)
for start in range(1,n+1):
    val = 0
    vals = []
    already_set = set()
    curr_mass = start
    while True:
        next_mass = pl[curr_mass]
        point = cl[next_mass]
        if next_mass in already_set:
            break
        else:
            vals.append(point)
            already_set.add(next_mass)
            curr_mass = next_mass
    # print(vals)
    if k <= len(vals):
        c_max = vals[0]
        c_val = vals[0]
        # if len(vals) > 1:
        for v in vals[1:k]:
            c_val += v
            c_max = max(c_max, c_val)
        # print(c_max)
        ans = max(c_max,ans)
    else:
        v_sum = sum(vals)
        if v_sum <= 0:
            c_max = vals[0]
            c_val = vals[0]
            # if len(vals) > 1:
            for v in vals[1:]:
                c_val += v
                c_max = max(c_max, c_val)
            # print(c_max)
            ans = max(c_max,ans)
        else:
            if k%len(vals) > 0:
                loop_cnt = k//len(vals)
                rem = k - loop_cnt*len(vals)
                c_max = v_sum*loop_cnt
                c_val = v_sum*loop_cnt
                if rem > 0:
                    for v in vals[:rem]:
                        c_val += v
                        c_max = max(c_max, c_val)
                # print(c_max)
                ans = max(c_max,ans)
            else:
                loop_cnt = k//len(vals) - 1
                rem = len(vals)
                c_max = v_sum*loop_cnt
                c_val = v_sum*loop_cnt
                if rem > 0:
                    for v in vals[:rem]:
                        c_val += v
                        c_max = max(c_max, c_val)
                # print(c_max)
                ans = max(c_max,ans)
    # print(c_max)
print(ans)
# 2939275739
