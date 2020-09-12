x = int(input())
ans = 0
for i in range(33):
    for j in range(2,11):
        if pow(i,j) > x: break
        ans = max(ans,pow(i,j))

print(ans)