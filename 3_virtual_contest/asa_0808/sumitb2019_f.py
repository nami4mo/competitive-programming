t1,t2 = map(int, input().split())
a1,a2 = map(int, input().split())
b1,b2 = map(int, input().split())

if a1 > b1 and a2 > b2:
    print(0)
    exit()

if b1 > a1 and b2 > a2:
    print(0)
    exit()

if a1 < b1 and a2 > b2:
    a1,b1 = b1,a1
    a2,b2 = b2,a2 


diff1 = abs(a1-b1)
diff2 = abs(a2-b2)

first_dist = diff1*t1
second_dist = diff2*t2

down = second_dist - first_dist
if down < 0:
    print(0)
    exit()
if down == 0:
    print('infinity')
    exit()

if first_dist%down != 0:
    ans = (first_dist//down) * 2 + 1
else:
    ans = ((first_dist//down)-1) * 2 + 2

print(ans)