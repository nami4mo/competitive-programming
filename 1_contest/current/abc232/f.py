

def main():
    n, x, y = map(int, input().split())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))

    INF = 10**18
    dp = [INF]*(1 << n)
    dp[0] = 0
    for i in range(1 << n):
        pc = bin(i).count("1")
        zero = 0
        for j in range(n):
            if i & (1 << j):
                continue
            bits = i | (1 << j)
            zero += 1
            j_pos = pc+zero-1

            dist = abs(pc-j_pos)
            cost_y = dist*y
            cost_x = abs(bl[pc]-al[j])*x
            # print(bits)
            dp[bits] = min(dp[bits], dp[i]+cost_x+cost_y)
    # print(dp)
    print(dp[-1])


if __name__ == "__main__":
    main()
