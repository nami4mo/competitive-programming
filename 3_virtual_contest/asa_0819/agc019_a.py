q,h,s,d = map(int, input().split())
n = int(input())

q = 4*q
h = 2*h

min_1 = min(q,h,s)
if n == 1:
    print(min_1)
else:
    if min_1*2 < d:
        print(n*min_1)
    else:
        double = n//2
        v = double*d
        if n%2 == 1:
            v += min_1
        print(v)