
x = int(input())
bekis = set()
bekis.add(1)

ans = 1
for b in range(2,35):
    for p in range(2,11):
        num = pow(b,p)
        if num <= x:
            ans = max(ans,num)
        else:
            break
print(ans)