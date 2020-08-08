n,k = map(int, input().split())

if k == 0:
    print(n**2)
    exit()

ans = 0
for b in range(1,n+1):
    one_loop_k = b-k
    if one_loop_k <=  0: continue
    loop_cnt = n//b
    ans += one_loop_k*loop_cnt

    rem = n-loop_cnt*b
    ans += max(0,rem-k+1)
    # print(b,ans)

print(ans)