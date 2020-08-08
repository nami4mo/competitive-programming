n = int(input())
al = list(map(int, input().split()))
al.sort()

c_sum = al[0]
cnt = 1
for a in al[1:]:
    if c_sum*2 >= a:
        c_sum += a
        cnt += 1
    else:
        c_sum += a
        cnt = 1

print(cnt)