from itertools import product

n,m = map(int, input().split())
xyzl = []
for _ in range(n):
    x,y,z = map(int, input().split())
    xyzl.append((x,y,z))

# if m==0: 
#     print(0)
#     exit()

ans = 0
for xs in [1, -1]:
    for ys in [1, -1]:
        for zs in [1, -1]:
            curr_sums = []
            for xyz in xyzl:
                x,y,z = xyz
                x*=xs
                y*=ys
                z*=zs
                curr_sums.append(x+y+z)
            curr_sums.sort()
            ans = max(ans, sum(curr_sums[-m:]))

print(ans)