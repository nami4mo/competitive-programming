r1,c1 = map(int, input().split())
r2,c2 =map(int, input().split())

if r1 == r2 and c1 == c2:
    print(0)
    exit()

if abs(r1-r2) == abs(c1-c2):
    print(1)
    exit()

d = abs(r1-r2) + abs(c1-c2)
if d <= 3:
    print(1)
    exit()

if d <= 6:
    print(2)
    exit()

if abs(abs(r1-c1)-abs(r2-c2)) <= 3:
    print(2)
    exit()

if d%2 == 0:
    print(2)
else:
    y1 = r2-c2
    y2 = r2+c2
    p1 = r1+y1
    p2 = -r1+y1
    p3 = c1-y1
    p4 = y2-c1
    d1 = abs(c1-p1)
    d2 = abs(c1-p2)
    d3 = abs(r1-p3)
    d4 = abs(r1-p4)

    dm = min(d1,d2,d3,d4)
    if dm <= 3:
        print(2)
    else:
        print(3)
        
    

# y1 = r2-c2

# y2 = r2+c2

# p1 = r1+y1
# p2 = -r1+y1
# p3 = c1-y1
# p4 = y2-c1

# d1 = abs(c1-p1)
# d2 = abs(c1-p2)
# d3 = abs(r1-p3)
# d4 = abs(r1-p4)

# d = min(d1,d2,d3,d4)
# d = (d-1)//3 + 1

# ans1 = d+1

# ans2 = 

