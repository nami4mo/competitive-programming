n,a,b = map(int, input().split())
diff = abs(a-b)
if diff%2 == 0:
    print(diff//2)
else:
    near = min(abs(a-1), abs(n-b))
    ans = near + (diff+1)//2
    print(ans)