n=int(input())
al=list(map(int, input().split()))
ans=0
for a in al:
    if a>=10:ans+=(a-10)
print(ans)