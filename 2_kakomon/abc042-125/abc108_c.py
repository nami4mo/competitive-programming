n, k = map(int, input().split())

k_multi_cnt = n//k
ans = pow(k_multi_cnt,3)

if k%2 == 0:
    half_cnt = (n+k//2)//k
    ans += pow(half_cnt,3)

print(ans)