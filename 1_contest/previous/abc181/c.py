from math import gcd

n = int(input())
xyl = []
for _ in range(n):
    x,y = map(int, input().split())
    xyl.append((x,y))

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            dx1 = xyl[i][0] - xyl[j][0]
            dy1 = xyl[i][1] - xyl[j][1]
            dx2 = xyl[i][0] - xyl[k][0]
            dy2 = xyl[i][1] - xyl[k][1]
            if dx1 == 0:
                if dx2 == 0:
                    # print(i,j,k)
                    print('Yes')
                    exit()
            elif dx2 == 0:
                if dx1 == 0:
                    # print(i,j,k)

                    print('Yes')
                    exit()
            elif dy1 == 0:
                if dy2 == 0:
                    # print(i,j,k)

                    print('Yes')
                    exit()
            elif dy2 == 0:
                if dy1 == 0:
                    # print(i,j,k)

                    print('Yes')
                    exit()
            else:
                gcd1 = gcd(dx1,dy1)
                gcd2 = gcd(dx2,dy2)
                dx1,dy1 = dx1//gcd1, dy1//gcd1
                dx2,dy2 = dx2//gcd2, dy2//gcd2
                if dx1 < 0:
                    dx1*=-1
                    dy1*=-1
                if dx2 < 0:
                    dx2*=-1
                    dy2*=-1
                if dx1 == dx2 and dy1 == dy2:
                    # print(i,j,k)
                    
                    print('Yes')
                    exit()

print('No')