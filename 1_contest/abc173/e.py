
def main():
    MOD = 10**9+7
    n,k = map(int, input().split())
    al = list(map(int, input().split()))
    al_abs = []
    al_nl = []
    for a in al: 
        if a > 0: sig = 1
        elif a < 0 : 
            sig = -1
            al_nl.append(a)
        else: sig = 0
        al_abs.append((abs(a), sig))

    if n == k:
        ans = 1
        for i in range(k):
            a = al[i]
            ans *= a
            ans %= MOD
        print(ans)
        exit()

    al_abs.sort(reverse=True)
    n_cnt = 0
    last_p = -1
    last_n = -1
    for i in range(k):
        a, sig = al_abs[i]
        if sig == -1:
            n_cnt+=1
            last_n = i
        elif sig == 1:
            last_p = i
    
    ans = 1
    if n_cnt%2 == 0:
        for i in range(k):
            a, sig = al_abs[i]
            ans *= a
            ans %= MOD
        print(ans)
        exit()


    next_p = -1
    next_n = -1 
    for i in range(k,n):
        a, sig = al_abs[i]
        if sig == 1 and next_p == -1:
            next_p = i
        elif sig == -1 and next_n == -1:
            next_n = i
        if next_n != -1 and next_p != -1:
            break

    comp_np = 0
    if next_p != -1:
        last_n_val = al_abs[last_n][0]
        next_p_val = al_abs[next_p][0]
        comp_np = next_p_val*(1.0)/last_n_val

    comp_pn = 0
    if next_n != -1 and last_p != -1:
        last_p_val = al_abs[last_p][0]
        next_n_val = al_abs[next_n][0]
        comp_pn = next_n_val*(1.0)/last_p_val

    if comp_np == 0 and comp_pn > 0:
        np_or_pn = False
    elif comp_pn == 0 and comp_np > 0:
        np_or_pn = True
    elif comp_np > 0 and comp_pn > 0:
        if next_p_val*last_p_val > next_n_val*last_n_val:
            np_or_pn = True
        else:
            np_or_pn = False

    elif comp_np == 0 and comp_pn == 0:
        if 0 in al:
            print(0)
            exit()
        else:
            al_nl.sort(reverse=True)
            for i in range(k):
                a = al_nl[i]
                ans *= (a)
                ans %= MOD
            print(ans)
            exit()


    # print(next_p, next_n, comp_np, comp_pn)

    for i in range(k):
        if np_or_pn and i == last_n:
            continue
        if (not np_or_pn) and i == last_p:
            continue
        a, sig = al_abs[i]
        ans *= a
        ans %= MOD

    if np_or_pn:
        ans *= next_p_val
        ans %= MOD
    else:
        ans *= next_n_val
        ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()