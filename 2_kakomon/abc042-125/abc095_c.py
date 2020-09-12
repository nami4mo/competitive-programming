a,b,c,x,y = map(int, input().split()) 

if a + b <= 2*c:
    print(a*x+b*y)
else:
    ab_cnt = min(x,y)
    remain_a = x-ab_cnt
    remain_b = y-ab_cnt


    if remain_a > 0 and a > 2*c:
        print(ab_cnt*2*c + remain_a*2*c)
    elif remain_b > 0 and b > 2*c:
        print(ab_cnt*2*c + remain_b*2*c)
    else:
        print(ab_cnt*2*c + remain_a*a + remain_b*b)