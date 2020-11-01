x,y = map(int, input().split())
ans = 1
for i in range(10**5):
    x*=2
    if x <= y: ans+=1
    else: break
print(ans)
