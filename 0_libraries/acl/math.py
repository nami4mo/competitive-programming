def sum_of_floor(n,m,a,b):
    ans = 0
    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m
    if b >= m:
        ans += n * (b // m)
        b %= m
    y_max = (a * n + b) // m
    x_max = (y_max * m - b)
    if y_max == 0: 
        return ans
    ans += (n - (x_max + a - 1) // a) * y_max
    ans += sum_of_floor(y_max, a, m, (a - x_max % a) % a)
    return ans
