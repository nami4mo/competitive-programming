n,k = map(int, input().split())

ok = [ [0]*k for _ in range(k) ]
ng = [ [0]*k for _ in range(k) ]

ok_cnt = 0
ng_cnt = 0
for _ in range(n):
    x,y,c = map(str, input().split())
    x = int(x)%(k*2)
    y = int(y)%(k*2)
    if (x < k and y < k and c=='W') or (x >= k and y >= k and c=='W') or (x < k and y>= k and c =='B') or (x >= k and y < k and c =='B'):
        ok[x%k][y%k] += 1
        ok_cnt += 1
    else:
        ng[x%k][y%k] += 1
        ng_cnt += 1

ok_csums = [ [0]*(k+1) for _ in range(k+1)]
for i in range(k):
    for j in range(k):
        ok_csums[i+1][j+1] = ok_csums[i+1][j] + ok_csums[i][j+1] - ok_csums[i][j] + ok[i][j]

ng_csums = [ [0]*(k+1) for _ in range(k+1)]
for i in range(k):
    for j in range(k):
        ng_csums[i+1][j+1] = ng_csums[i+1][j] + ng_csums[i][j+1] - ng_csums[i][j] + ng[i][j]

    
ans = max(ok_cnt, ng_cnt)

# l u r b
for i in range(0,k+1):
    for j in range(0,k+1):
        ok_sum = ok_csums[i][j]
        ok_sum += (ok_csums[k][k] - ok_csums[i][k]- ok_csums[k][j] + ok_csums[i][j])
        ng_sum = ng_csums[i][k] - ng_csums[i][j]
        ng_sum += (ng_csums[k][j] - ng_csums[i][j])

        # ng_sum = 2*ng_cnt - ng_sum
        ans = max(ok_sum+ng_sum, ans)

for i in range(0,k+1):
    for j in range(0,k+1):
        ok_sum = ok_csums[i][k] - ok_csums[i][j]
        ok_sum += (ok_csums[k][j] - ok_csums[i][j])
        ng_sum = ng_csums[i][j]
        ng_sum += (ng_csums[k][k] - ng_csums[i][k]- ng_csums[k][j] + ng_csums[i][j])
        # ng_sum -= 2*ng_cnt
        # ng_sum = 2*ng_cnt - ng_sum
        ans = max(ok_sum+ng_sum, ans)


# # l u
# for i in range(1,k+1):
#     for j in range(1,k+1):
#         ok_sum = ok_csums[i][j]
#         ng_sum = ng_cnt - ng_csums[i][j]
#         ans = max(ok_sum+ng_sum, ans)

# # r b
# for i in range(0,k):
#     for j in range(0,k):
#         ok_sum = ok_csums[k][k] - ok_csums[i][k]-ok_csums[k][j] + ok_csums[i][j]
#         ng_sum = ng_cnt - (ng_csums[k][k] - ng_csums[i][k]-ng_csums[k][j] + ng_csums[i][j])
#         ans = max(ok_sum+ng_sum, ans)

# # l b
# for i in range(0,k):
#     for j in range(1,k+1):
#         ok_sum = ok_csums[k][j] - ok_csums[i][j]
#         ng_sum = ng_cnt - (ng_csums[k][j] - ng_csums[i][j])
#         ans = max(ok_sum+ng_sum, ans)


# # r u
# for i in range(1,k+1):
#     for j in range(0,k):
#         ok_sum = ok_csums[i][k] - ok_csums[i][j]
#         ng_sum = ng_cnt - (ng_csums[i][k] - ng_csums[i][j])
#         ans = max(ok_sum+ng_sum, ans)


print(ans)