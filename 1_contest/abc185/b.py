n,m,t=map(int, input().split())
man = n

prev_a = 0
prev_b = 0
for _ in range(m):
    a,b=map(int, input().split())
    n -= (a-prev_b)
    if n <= 0:
        print('No')
        exit()
    n += (b-a)
    n = min(man,n)
    prev_b = b

n -= (t-prev_b)
if n <= 0:
    print('No')
    exit()

print('Yes')