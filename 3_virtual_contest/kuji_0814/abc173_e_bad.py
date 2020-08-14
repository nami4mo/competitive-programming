n, k = map(int, input().split())
al = list(map(int, input().split()))
al_abs = []
al_p = []
al_m = []
zero_cnt = 0
MOD = 10**9+7

if n == 1 and k == 1:
    print(al[0]%MOD)
    exit()

if n == k:
    ans = 1
    for a in al:
        ans *= a
        ans %= MOD
    print(ans)
    exit()

for a in al:
    if a == 0:
        zero_cnt+=1
    else:
        if a > 0: 
            al_abs.append((abs(a),1))
            al_p.append(a)
        elif a < 0: 
            al_abs.append((abs(a),-1))

al_abs.sort(reverse=True)
if len(al_abs) < k:
    print(0)
    exit()

if len(al_abs) == k:
    ans = 1
    m_cnt = 0
    for a,s in al_abs:
        if s == -1: m_cnt += 1
        ans *= a
        ans %= MOD
    if m_cnt%2 == 0:
        print(ans)
    else:
        print(0)
    exit()
    

if not al_p:
    if k%2 == 1 and zero_cnt > 0:
        print(0)
    else:
        if k%2 == 1:
            al_abs.sort()
        ans = 1
        for a,s in al_abs[:k]:
            ans *= (a*(-1))
            ans %= MOD
        print(ans)
    exit()



val = 1
m_cnt = 0
last_m = 0
last_p = 0
for i in range(k):
    v,sig = al_abs[i]
    val *= v
    val %= MOD
    if sig == -1:
        m_cnt += 1
        last_m = v
    else:
        last_p = v

if m_cnt %2 == 0:
    print(val)
    exit()


# minus -> plus 

## search next p
next_p = 0
for i in range(k,len(al_abs)):
    v,sig = al_abs[i]
    if sig == 1:
        next_p = v
        break

## search next m
next_m = 0
for i in range(k,len(al_abs)):
    v,sig = al_abs[i]
    if sig == -1:
        next_m = v
        break

# print(next_m, next_p)

if next_p == 0 and next_m == 0:
    print(0)
    exit()

# last_m -> next_p
if next_p*last_p >= next_m*last_m or last_p == 0:
# if next_p > 0 and next_m == 0:
    ans = 1
    skip_flag = False
    for i in range(k):
        v,sig = al_abs[i]
        if not skip_flag and v == last_m and sig == -1:
            ans *= next_p
            skip_flag = True
        else:
            ans *= v
        # print(ans)
        ans %= MOD
    print(ans)
    exit()


# last_p -> next_m
# if next_p == 0 and next_m > 0:
elif next_p*last_p <= next_m*last_m:
    ans = 1
    skip_flag = False
    for i in range(k):
        v,sig = al_abs[i]
        if not skip_flag and v == last_p and sig == 1:
            ans *= next_m
            skip_flag = True
        else:
            ans *= v
        ans %= MOD
    print(ans)
    exit()