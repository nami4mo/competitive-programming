n = int(input())
al = list(map(int, input().split()))
sum_d = {0:1}
c_sum = 0
ans = 0
for a in al:
    c_sum += a
    sum_d.setdefault(c_sum,0)
    ans += sum_d[c_sum]
    sum_d[c_sum] += 1

print(ans)