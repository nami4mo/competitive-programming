n = int(input())    
al = list(map(int, input().split()))    
al.sort(reverse=True)

ans = al[0]
for i in range(n-2):
    ans += al[i//2+1]

print(ans)