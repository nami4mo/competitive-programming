from collections import deque

n,k = map(int, input().split())
al = list(map(int, input().split()))

for a1,a2 in zip(al[0:n-k], al[-(n-k):]):
    # print(a1,a2)
    if a1 < a2:
        print('Yes')
    else:
        print('No')
