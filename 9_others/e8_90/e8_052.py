n=int(input())
asums=[sum(list(map(int, input().split()))) for _ in range(n)]
ans=1
MOD=10**9+7
for a in asums: ans=(ans*a)%MOD
print(ans)