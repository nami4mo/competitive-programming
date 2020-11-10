from math import ceil
n,x = map(int, input().split())
al = list(map(int, input().split()))

ans = 0
st = set()
vs = []
for i in range(n-1,-1,-1):
    pattern = 1
    over = ceil(x/al[i])
    v = over*al[i]-x
    if v in st: continue
    st.add(v)
    vs.append(v)
    new_vs = [over*al[i]]
    for j in range(n):
        for v in new_vs:
            rem = v-x
            for k in range(n-1,j,-1):
                cnt = rem//al[i]
                rem -= cnt*al[i]
            if rem >= al[j]:
                print(al[j])
                pattern *= 2
                cntt = ceil(rem/al[j])
                new_vs.append(over*al[i]+al[j]*cntt)
    # vs = new_vs[:]
    for nv in new_vs:
        if nv not in vs:
            vs.append(nv)
    ans += pattern
    print('====',al[i], ans)

print(ans)