
n = int(input())
al = []
bl = []
for _ in range(n):
    a,b = map(int, input().split())
    al.append(a)
    bl.append(b)

al.sort()
bl.sort()

if n%2 == 1:
    mmin = al[n//2]
    mmax = bl[n//2]
    print(mmax-mmin+1)
else:
    mmin = (al[n//2]+al[n//2-1])/2
    mmax = (bl[n//2]+bl[n//2-1])/2
    ans = (mmax-mmin)*2+1
    ans = round(ans+0.1)
    print(ans)