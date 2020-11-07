a,b = map(int, input().split())
if a > 0:
    print('Positive')
elif a == 0:
    print('Zero')
else:
    if b >= 0:
        print('Zero')
    else:
        minus_cnt = b-a+1
        if minus_cnt%2 == 0:
            print('Positive')
        else:
            print('Negative')