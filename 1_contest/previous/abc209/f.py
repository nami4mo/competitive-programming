n=int(input())
hl=list(map(int, input().split()))

dp_saki=[0]*n
dp_ato=[0]*n

for i in range(n):
    h=hl[i]
    