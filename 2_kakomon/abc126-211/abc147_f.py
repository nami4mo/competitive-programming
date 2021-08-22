INF = 10**18
n,x,d = map(int, input().split())

if d == 0:
    if x == 0:
        print(1)
        exit()
    else:
        print(n+1)
        exit()

# g=gcd(x,d)
# x,d = x//g, d//g

if d < 0:
    d*=-1
    x*=-1

mod_lrs = {}

last_a = x+(n-1)*d

for num in range(0,n+1):
    c_mod = (x*num)%d
    if not c_mod in mod_lrs: mod_lrs[c_mod] = []

    left = num*(2*x+(num-1)*d)//2
    right = num*(2*last_a+(num-1)*d*(-1))//2
    
    mod_lrs[c_mod].append((left,1))
    mod_lrs[c_mod].append((right,-1))


ans = 0
for lrs in mod_lrs.values():
    lrs.sort(key=lambda x: (x[0],-x[1]))
    l_cnt = 0
    last_l = -INF
    for v, lr in lrs:
        if l_cnt == 0:
            l_cnt += 1
            last_l = v
        else:
            l_cnt += lr
            if l_cnt == 0:
                step = (v-last_l)//d+1
                ans += step
    
print(ans)