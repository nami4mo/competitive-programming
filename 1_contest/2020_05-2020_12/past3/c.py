def pow_k(x, n):
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2
        if K*x > 10**9:
            return -1
    return K * x




a, r, n = map(int, input().split()) 
ans = a*pow_k(r,n-1)
if ans < 0 or ans > 10**9:
    print('large')
else:
    print(ans)