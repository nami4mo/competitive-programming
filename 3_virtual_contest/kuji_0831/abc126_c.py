n ,k = map(int, input().split())

ans = 0
twol = [0]*20
for i in range(1,n+1): 
    two = 0
    curr_i = i
    for i in range(20):
        if curr_i >= k: break
        curr_i *= 2
        two += 1
    twol[two] += 1

ans = 0
for two, cnt in enumerate(twol):
    ans += cnt/pow(2,two)
    
ans /= n
print(ans)
# for i in range(20):
#     if pow(2,i) * n >= k:
