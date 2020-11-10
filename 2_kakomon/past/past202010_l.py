n,q = map(int, input().split())
hl = list(map(int, input().split()))

even_diff = {}
odd_diff = {}

for i in range(n-1):
    diff = hl[i+1]-hl[i]
    if i%2 == 0:
        if diff not in even_diff:
            even_diff[diff] = 0
        even_diff[diff]+=1
    else:
        if diff not in odd_diff:
            odd_diff[diff] = 0
        odd_diff[diff]+=1

even_up_sum = 0
ansl = []
for _ in range(q):
    ql = list(map(int, input().split()))
    if ql[0] == 1:
        even_up_sum += ql[1]
    elif ql[0] == 2:
        even_up_sum -= ql[1]
    else:
        u,v = ql[1],ql[2]
        u-=1
        if u%2 == 0:
            if u != 0:
                old_diff = hl[u]-hl[u-1]
                new_diff = old_diff + v
                odd_diff[old_diff] -= 1
                if new_diff not in odd_diff:
                    odd_diff[new_diff] = 0
                odd_diff[new_diff] += 1

            if u != n-1:
                old_diff = hl[u+1]-hl[u]
                new_diff = old_diff - v
                even_diff[old_diff] -= 1
                if new_diff not in even_diff:
                    even_diff[new_diff] = 0
                even_diff[new_diff] += 1

        else:
            if u != 0:
                old_diff = hl[u]-hl[u-1]
                new_diff = old_diff + v
                even_diff[old_diff] -= 1
                if new_diff not in even_diff:
                    even_diff[new_diff] = 0
                even_diff[new_diff] += 1

            if u != n-1:
                old_diff = hl[u+1]-hl[u]
                new_diff = old_diff - v
                odd_diff[old_diff] -= 1
                if new_diff not in odd_diff:
                    odd_diff[new_diff] = 0
                odd_diff[new_diff] += 1
        hl[u] += v
            

    ans = 0
    if even_up_sum in even_diff:
        ans += even_diff[even_up_sum]
    if (-1)*even_up_sum in odd_diff:
        ans += odd_diff[(-1)*even_up_sum]

    # print(even_diff)
    # print(odd_diff)

    ansl.append(ans)

for a in ansl: print(a)