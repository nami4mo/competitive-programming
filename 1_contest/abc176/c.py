n = int(input())
al = list(map(int, input().split()))   

ans = 0
prev = 0
for a in al:
    if prev <= a:
        prev = a
    else:
        rem = prev-a
        ans += rem

print(ans)