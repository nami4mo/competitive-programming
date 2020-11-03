import sys
input = sys.stdin.readline

ansl = []
for _ in range(int(input())):
    n = int(input())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    abl = []
    for i in range(n):
        abl.append((al[i],bl[i]))
    
    abl.sort(reverse=True, key=lambda x: x[0])

    deli_c = abl[0][0]
    # print(abl,'---')
    pic_c = 0
    ans = deli_c
    for i in range(n):
        deli_c = abl[i+1][0] if i+1 < n else 0
        pic_c += abl[i][1]
        ans = min(ans, max(deli_c,pic_c))

    # print(ans)
    ansl.append(ans)

for a in ansl: print(a)