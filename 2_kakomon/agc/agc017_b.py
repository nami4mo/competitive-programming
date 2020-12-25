n,a,b,c,d = map(int, input().split())
target = abs(b-a)
step = n-1

for posi_cnt in range(step+1):
    nega_cnt = step-posi_cnt
    
    posi_min = c*posi_cnt
    posi_max = d*posi_cnt

    nega_min = c*nega_cnt
    nega_max = d*nega_cnt

    ma = posi_max-nega_min
    mi = posi_min-nega_max

    if mi <= target <= ma:
        print('YES')
        break

else:
    print('NO')