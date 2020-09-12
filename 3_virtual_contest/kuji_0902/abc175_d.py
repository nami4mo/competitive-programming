n,k = map(int, input().split())
pl = [0] + list(map(int, input().split()))
cl = [0] + list(map(int, input().split()))

valsl = []
already = [False]*(n+1)
for i in range(1,n+1):
    if already[i]: continue
    vals = [cl[i]]
    curr_i = i
    already[i] = True
    while True:
        next_i = pl[curr_i]
        if already[next_i]: break
        v = cl[next_i]
        vals.append(v)
        curr_i = next_i
        already[next_i] = True
    valsl.append(vals)


# print(valsl)
ans = -10**18
for vals in valsl:
    curr_sum = sum(vals)
    vlen = len(vals)
    for i in range(len(vals)):
        new_vals = vals[i:] + vals[0:i]
        if curr_sum <= 0:
            vmax = -10**18
            v = 0
            for j in range(min(k,vlen)):
                v += new_vals[j]
                vmax = max(v,vmax)
            ans = max(vmax, ans)
        else:
            loop = k//vlen-1
            rem = k-loop*vlen
            v = loop*curr_sum
            vmax = v
            for j in range(rem):
                v += new_vals[j%vlen]
                vmax = max(v,vmax)
            ans = max(vmax, ans)

print(ans)