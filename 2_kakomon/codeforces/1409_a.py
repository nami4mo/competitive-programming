t=int(input())
for _ in range(t):
    a,b = map(int, input().split())
    d = abs(a-b)
    ans = (d-1)//10 +1
    print(ans)