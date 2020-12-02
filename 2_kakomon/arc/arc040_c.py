n = int(input())
sl = []
for _ in range(n):
    sl.append(input())

ans = 0
prev_r = -1
for i, s in enumerate(sl):
    if prev_r == -1:
        r = 0
        for j in range(n-1,-1,-1):
            if s[j] == '.':
                prev_r = j
                break
        else:
            prev_r = -1
            continue
        ans += 1
    
    else:
        most_l = n-1
        for j in range(prev_r):
            if s[j] == '.': most_l = j
        if most_l >= prev_r:
            prev_r = -1
        else:
            ans += 1
            prev_r = most_l

print(ans)

