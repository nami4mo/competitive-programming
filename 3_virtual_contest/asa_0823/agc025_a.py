n = int(input())
ans = 10**9
for a in range(1,n):
    b = n - a
    a_sum = 0
    b_sum = 0
    for ai in str(a):
        a_sum += int(ai)
    for bi in str(b):
        b_sum += int(bi)
    v = a_sum+b_sum
    ans = min(ans,v)

print(ans)