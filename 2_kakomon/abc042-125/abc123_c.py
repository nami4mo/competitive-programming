n = int(input())
mmin = 10**16
for _ in range(5):
    x = int(input())
    mmin = min(mmin,x)

ans = (n-1)//mmin + 5
print(ans)