a,b = map(int, input().split())
if (a-b)%2 == 1:
    print('IMPOSSIBLE')
else:
    ans = abs(a-b)//2 + min(a,b)
    print(ans)    
