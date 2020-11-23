n,x =map(int, input().split())
s=input()

for si in s:
    if si == 'x':
        x -= 1
        x = max(0,x)
    else:
        x += 1

print(x)