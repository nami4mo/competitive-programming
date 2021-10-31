from math import gcd
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    al = list(map(int, input().split()))
    al.sort(reverse=True)

    first = al[0]
    c_gcd = first
    ans = [first]
    used = [False]*(n)
    used[0] = True
    for _ in range(n-1):
        a = 0
        v = 0
        vi = -1
        for i in range(1,n):
            if used[i]: continue
            curr_v = gcd(c_gcd, al[i])
            if curr_v > v:
                v = curr_v
                vi = i
                a = al[i]
            elif curr_v == v and a > al[i]:
                v = curr_v
                vi = i
                a = al[i]
        ans.append(a)
        used[vi] = True
        c_gcd = v

    print(*ans)
