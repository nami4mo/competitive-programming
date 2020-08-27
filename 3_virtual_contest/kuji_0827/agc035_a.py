n = int(input())
al = list(map(int, input().split()))
al.sort()
al_cnt_d = {}

if al[0] == 0 and al[n-1] == 0:
    print('Yes')

elif n == 3:
    if al[0] ^ al[1] ^al[2] == 0:
        print('Yes')
    else:
        print('No')

elif n%3 == 0:
    for a in al:
        al_cnt_d.setdefault(a,0)
        al_cnt_d[a] += 1

    if len(al_cnt_d) == 3:
        val = 0
        for k,v in al_cnt_d.items():
            val = val^k
            if v != n//3:
                print('No')
                exit()
        if val == 0: print('Yes')
        else: print('No')
    elif len(al_cnt_d) == 2:
        if 0 not in al_cnt_d or al_cnt_d[0] != n//3:
            print('No')
            exit()            
        else:
            print('Yes')
    else:
        print('No')


else:
    print('No')