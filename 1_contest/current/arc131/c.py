n=int(input())
al=list(map(int, input().split()))

if n%2==1:
    print('Win')
    exit()

v=0
for a in al:
    v^=a

ok=False
for a in al:
    if v==a:
        ok=True

if (n%2==0 and ok) or (n%2==1 and not ok):
    print('Win')
else:
    print('Lose')
