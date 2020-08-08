n = int(input())
al = list(map(int, input().split()))

al_sum = sum(al)
if al_sum%n != 0:
    print(-1)
    exit()

k = al_sum//n

ans = 0
curr_num = al[0]
curr_cnt = 1
for a in al[1:]:
    if curr_cnt*k == curr_num:
        curr_num = a
        curr_cnt = 1
    else:
        ans += 1
        curr_num += a
        curr_cnt += 1
print(ans)