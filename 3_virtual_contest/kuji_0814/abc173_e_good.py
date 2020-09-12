def modinv(a,m):
    b, u, v = m, 1, 0
    while b:
        t = a//b
        a -= t*b
        a,b = b,a
        u -= t * v
        u,v = v,u
    u %= m
    return u


n, k = map(int, input().split())
al = list(map(int, input().split()))
al_abs = []
al_p = []
al_m = []
zero_cnt = 0
MOD = 10**9+7

for a in al:
    if a == 0:
        zero_cnt+=1
    elif a > 0: 
        al_abs.append((abs(a),1))
        al_p.append(a)
    else: 
        al_abs.append((abs(a),-1))
        al_m.append(abs(a))
al_abs.sort(reverse=True)


if n == k:
    ans = 1
    for a in al:
        ans *= a
        ans %= MOD
    print(ans)
    exit()


if len(al_abs) < k:
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


next_p = 0
for i in range(k,len(al_abs)):
    v,sig = al_abs[i]
    if sig == 1:
        next_p = v
        break

next_m = 0
for i in range(k,len(al_abs)):
    v,sig = al_abs[i]
    if sig == -1:
        next_m = v
        break

if next_p == 0 and next_m == 0:
    print(0)
    exit()

if next_p*last_p >= next_m*last_m or last_p == 0:
    ans = val*modinv(last_m%MOD,MOD)*next_p
    ans %= MOD
    print(ans)

else:
    ans = val*modinv(last_p%MOD,MOD)*next_m
    ans %= MOD
    print(ans)