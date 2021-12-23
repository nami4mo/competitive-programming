

def main():
    h, w, k = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    dp1 = [0]*(k+1)
    dp2x = [0]*(k+1)
    dp2y = [0]*(k+1)
    dp3 = [0]*(k+1)

    if x1 == x2 and y1 == y2:
        dp1[0] = 1
    elif x1 == x2:
        dp2x[0] = 1
    elif y1 == y2:
        dp2y[0] = 1
    else:
        dp3[0] = 1

    MOD = 998244353
    for i in range(k):
        dp1[i+1] = dp2x[i]+dp2y[i]
        dp2x[i+1] = dp1[i]*(w-1)+dp2x[i]*(w-2)+dp3[i]
        dp2y[i+1] = dp1[i]*(h-1)+dp2y[i]*(h-2)+dp3[i]
        dp3[i+1] = dp2x[i]*(h-1)+dp2y[i]*(w-1)+dp3[i]*(h+w-4)
        dp1[i+1] %= MOD
        dp2x[i+1] %= MOD
        dp2y[i+1] %= MOD
        dp3[i+1] %= MOD
    print(dp1[k])


if __name__ == "__main__":
    main()
