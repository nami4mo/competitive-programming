t=int(input())
for _ in range(t):
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))

    min21 = min(al[2],bl[1])
    ans = 2*min21
    al[2] -= min21
    bl[1] -= min21

    if bl[2] <= al[0]+al[2]:
        print(ans)
    else:
        rem = bl[2]-al[0]-al[2]
        ans -= 2*rem
        print(ans)