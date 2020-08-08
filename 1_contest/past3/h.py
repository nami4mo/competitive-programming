n, l = map(int, input().split()) 
x_list = list(map(int, input().split())) 
hardle = set(x_list)
t1, t2, t3 = map(int, input().split()) 

dp = [-1] * (l+10)
dp[0] = 0
dp[1] = t1
if 1 in x_list:
    dp[1] += t3

for i in range(2, l+10):
    t3_loss = 0
    if i in hardle: t3_loss = t3

    run1 = t1 + dp[i-1] + t3_loss
    run2 = t1 + t2 + dp[i-2] + t3_loss
    if i < 4:
        run3 = 99999999
    else:
        run3 = t1 + 3*t2 + dp[i-4] + t3_loss
    dp[i] = min(run1, run2, run3)


# last
g0 = dp[l]

g1 = dp[l-1] + t1
g2 = dp[l-1] + t2//2 + t1//2

g3 = dp[l-2] + t1 + t2
g4 = dp[l-2] + t1//2 + 3*t2//2

g5 = dp[l-3] + t1//2 + 5*t2//2
print( min(g0,g1,g2,g3,g4,g5) )