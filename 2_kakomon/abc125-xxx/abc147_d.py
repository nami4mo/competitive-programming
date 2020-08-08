def main():
    MOD = 10**9+7
    n = int(input())
    al = list(map(int, input().split()))

    base_2_cnt = [0]*60 
    for a in al:
        for i in range(60):
            if ((a >> i) & 1): base_2_cnt[i] += 1

    ans = 0
    curr_2 = 1
    for i in range(60):
        base_01_comb = base_2_cnt[i] * (n-base_2_cnt[i])
        ans += base_01_comb * curr_2
        ans %= MOD
        curr_2*=2
        curr_2%=MOD

    print(ans%MOD)

if __name__ == "__main__":
    main()