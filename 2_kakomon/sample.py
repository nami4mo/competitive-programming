a,b,k = map(int, input().split())

if k <= a:
    print(a-k,b)
else:
    rem = k-a
    if rem <= b:
        print(0, b-rem)
    else:
        print(0,0)