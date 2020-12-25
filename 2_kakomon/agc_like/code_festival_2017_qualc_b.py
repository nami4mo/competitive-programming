n=int(input())
al=list(map(int, input().split()))
ans=3**n
all_eve=1
for a in al:
    if a%2==0:all_eve*=2

print(ans-all_eve)