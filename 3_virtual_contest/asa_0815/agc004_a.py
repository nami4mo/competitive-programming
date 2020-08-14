ll = list(map(int, input().split()))
ll.sort()
if ll[0]%2 == 1 and ll[1]%2 == 1 and ll[2] %2 == 1:
    v = min(ll[0]*ll[1],ll[1]*ll[2],ll[2]*ll[0])
    print(v)
else:
    print(0) 