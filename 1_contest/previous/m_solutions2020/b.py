a,b,c = map(int, input().split())
k = int(input())

for _ in range(k):
    if c <= b or c <= a:
        c*=2
    elif b <= a:
        b*=2
        
    if a < b and b < c:
        print('Yes')
        break
else:
    print('No')