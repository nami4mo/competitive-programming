s=input()
s=s.replace('25','x')

ans = 0
cnt = 0
for si in s:
    if si == 'x':
        cnt += 1
    else:
        ans += cnt*(cnt+1)//2
        cnt = 0
ans += cnt*(cnt+1)//2
print(ans)