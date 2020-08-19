n = int(input())
al = []
bl = []
for _ in range(n):
    a,b= map(int, input().split())
    al.append(a)
    bl.append(b)

al.sort()
bl.sort()

if n%2 == 1:
    minv = al[n//2]
    maxv = bl[n//2]
    print(maxv-minv+1)

else:
    minv2 = al[n//2] + al[n//2-1]
    maxv2 = bl[n//2] + bl[n//2-1]
    print(maxv2-minv2+1)