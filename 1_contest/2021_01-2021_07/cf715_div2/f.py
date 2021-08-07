import sys
input = sys.stdin.readline

ansl=[]
for _ in range(int(input())):
    n=int(input())
    al=list(map(int, input().split()))
    l=[]
    r=[]
    for a in al:
        if a%2==0:l.append(a)
        else:r.append(a)
    aa=l+r
    ansl.append(aa)
for aa in ansl:print(*aa)