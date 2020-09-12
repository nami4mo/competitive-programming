a,b,c,d,e,f = map(int, input().split())
waters = []
for i in range(31):
    for j in range(31):
        v = 100*a*i + 100*b*j
        if v <= f and v != 0:
            waters.append(v)

waters = list(set(waters))
ans_vol, ans_sug = waters[0], 0
for w in waters:
    rem = f - w
    max_s = e*w//100
    max_s = min(rem, max_s)
    for c_cnt in range(max_s//c+1):
        cs = c_cnt*c
        rem_d = max_s - cs
        d_cnt = rem_d//d
        ds = d_cnt*d
        sug = cs+ds
        vol = sug + w
        if ans_sug*vol < sug*ans_vol:
            ans_vol, ans_sug = vol, sug

print(ans_vol, ans_sug)
        