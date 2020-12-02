n,m=map(int, input().split())
t=1900*m+(n-m)*100
ts=t*(2**m)
print(ts)