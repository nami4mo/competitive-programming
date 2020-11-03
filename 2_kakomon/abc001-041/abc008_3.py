n = int(input())
al = []
for _ in range(n):
    al.append(int(input()))

# al.sort()
ans = 0
for a in al:
    cnt = 0
    for aa in al:
        if a%aa == 0:
            cnt+=1
    cnt -= 1
    if cnt%2 == 0:
        p = (cnt//2+1)/(cnt+1)
        ans += p
    else:
        p = (cnt//2+1)/(cnt+1)
        ans += p
print(ans)