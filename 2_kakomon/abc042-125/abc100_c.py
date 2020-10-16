n = int(input())
al = list(map(int, input().split()))

cnt = 0
for a in al:
    while a%2 == 0:
        a//=2
        cnt+=1

print(cnt)